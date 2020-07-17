from rest_framework import permissions

from dojo.authorization import is_authorized_product


class UserHasProductPermission(permissions.BasePermission):
    """
    @brief      To ensure that one user can only access authorized project
    """
    def has_object_permission(self, request, view, obj):
        return is_authorized_product(request.user, obj)


class UserHasReportGeneratePermission(permissions.BasePermission):
    """
    @brief      To ensure that one user can only access authorized project
    """
    def has_object_permission(self, request, view, obj):
        return is_authorized_product(request.user, obj.product)


class UserHasScanSettingsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_authorized_product(request.user, obj.product)


class UserHasScanPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_authorized_product(request.user, obj.scan_settings.product)
