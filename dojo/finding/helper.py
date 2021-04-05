import logging
from typing import Dict, Any, Tuple

from django.utils import timezone
from django.conf import settings
from fieldsignals import pre_save_changed
from dojo.models import Finding
from dojo.utils import get_current_user

logger = logging.getLogger(__name__)


# this signal is triggered just before a finding is getting saved
# and one of the status related fields has changed
# this allows us to:
# - set any depending fields such as mitigated_by, mitigated, etc.
# - update any audit log / status history
def pre_save_finding_status_change(sender, instance, changed_fields, **kwargs):
    # some code is cloning findings by setting id/pk to None, ignore those, will be handled on next save
    if not instance.id:
        logger.debug('ignoring save of finding without id')
        return

    logger.debug('%i: changed status fields pre_save: %s', instance.id, changed_fields)

    current_user = get_current_user()
    user = current_user if current_user.is_authenticated else None
    update_finding_status(instance, user, changed_fields)


# also get signal when id is set/changed so we can process new findings
pre_save_changed.connect(pre_save_finding_status_change, sender=Finding, fields=['id', 'active', 'verfied', 'false_p', 'is_Mitigated', 'mitigated', 'mitigated_by', 'out_of_scope', 'risk_accepted', 'duplicate'])


def update_finding_status(new_state_finding, user, changed_fields: Dict[str, Tuple[Any, Any]]) -> None:
    now = timezone.now()

    is_new_finding = (len(changed_fields) == 1) and ('id' in changed_fields)

    if is_new_finding or ('is_Mitigated' in changed_fields):
        if new_state_finding.is_Mitigated:
            new_state_finding.mitigated = new_state_finding.mitigated or now
            new_state_finding.mitigated_by = new_state_finding.mitigated_by or user
        else:
            new_state_finding.mitigated = None
            new_state_finding.mitigated_by = None

    if is_new_finding or ('duplicate' in changed_fields):
        if not new_state_finding.duplicate:
            new_state_finding.duplicate_finding = None

    new_state_finding.last_status_update = now


def can_edit_mitigated_data(user):
    return settings.EDITABLE_MITIGATED_DATA and user.is_superuser
