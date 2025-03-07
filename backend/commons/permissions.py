from rest_framework.permissions import BasePermission
from accounts.models import CustomUser


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


__all__ = [IsModerator, IsOwner]
