import logging
import datetime
from django.utils import timezone
from django.conf import settings

logger = logging.getLogger(__name__)


def update_finding_status(new_state_finding, request_user) -> bool:
    finding_status_changed = False

    if not new_state_finding.duplicate:
        new_state_finding.duplicate_finding = None

    # ensure mitigate timestamp is added or cleared based on is_Mitigated boolean
    if new_state_finding.is_Mitigated and new_state_finding.mitigated is None:
        finding_status_changed = True
        new_state_finding.mitigated = timezone.now()
        new_state_finding.mitigated_by = request_user
    elif not new_state_finding.is_Mitigated and new_state_finding.mitigated is not None:
        finding_status_changed = True
        new_state_finding.mitigated = None
        new_state_finding.mitigated_by = None

    return finding_status_changed
