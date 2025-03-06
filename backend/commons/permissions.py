from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from accounts.models import CustomUser


class IsReader(BasePermission):
    """Разрешает только чтение (GET, HEAD, OPTIONS)"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsModerator(BasePermission):
    """Разрешает действие только модераторам"""

    def has_permission(self, request, view):
        return CustomUser.objects.filter(
            pk=request.user.id, role=CustomUser.Role.MODERATOR
        ).exists()


class IsOwner(BasePermission):
    """Разрешает изменение только владельцу объекта"""

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id


__all__ = [IsReader, IsModerator, IsOwner, IsAuthenticated]
