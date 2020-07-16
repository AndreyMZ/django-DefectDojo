from typing import Optional

from social_core.backends.azuread_tenant import AzureADTenantOAuth2 as OriginalAzureADTenantOAuth2


class AzureADTenantOAuth2(OriginalAzureADTenantOAuth2):
	def get_user_details(self, response):
		result = super().get_user_details(response)

		# By default `AzureADTenantOAuth2` sets `username` to the value of "name" claim (equal to `fullname`).
		# Let's use something more similar to a username.
		# See also: <https://docs.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-userprincipalname>.
		upn: Optional[str] = response.get('upn')
		if upn is not None:
			result['username'] = upn.rsplit("@", maxsplit=1)[0]

		# Let's save the groups for later use in `dojo.social_auth.pipeline.user_groups`.
		# See also:
		#   - <https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims>
		#   - <https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims#configuring-groups-optional-claims>
		#   - <https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims>
		result['groups'] = response.get('groups', [])

		return result

	def auth_html(self):
		raise NotImplementedError()
