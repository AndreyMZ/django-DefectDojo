from django.contrib.auth.models import Group


def user_groups(strategy, details, backend, user=None, *args, **kwargs) -> None:
	"""Update user groups using data from provider."""

	if not user:
		return

	for group_name in details.get('groups', []):
		group, _ = Group.objects.get_or_create(name=group_name)
		user.groups.add(group)
