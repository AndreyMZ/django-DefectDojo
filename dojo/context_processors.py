# import the settings file
from django.conf import settings


def globalize_oauth_vars(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'LOGIN_GOOGLE_ENABLED':         settings.LOGIN_GOOGLE_ENABLED,
        'LOGIN_OKTA_ENABLED':           settings.LOGIN_OKTA_ENABLED,
        'LOGIN_AZUREAD_TENANT_ENABLED': settings.LOGIN_AZUREAD_TENANT_ENABLED
    }
