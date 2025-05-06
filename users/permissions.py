from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка является ли пользователй владельцем."""

    def has_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
