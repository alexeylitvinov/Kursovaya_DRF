from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Устанавливает права для пользователя.
    """
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
