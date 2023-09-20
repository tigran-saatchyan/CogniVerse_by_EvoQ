from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    message = "You are not Superuser"

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsManager(BasePermission):
    message = "You are not allowed to create or delete"

    def has_permission(self, request, view):
        return request.user.is_staff and request.method not in [
            "DELETE", "POST"
        ]
