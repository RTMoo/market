from rest_framework.permissions import BasePermission
from accounts.models import CustomUser


class IsModerator(BasePermission):
    """Разрешает действие только модераторам"""

    def has_permission(self, request, view):
        return CustomUser.objects.filter(
            pk=request.user.id, role=CustomUser.Role.MODERATOR
        ).exists()


class IsSeller(BasePermission):
    """Разрешает действие только продавцам"""

    def has_permission(self, request, view):
        return CustomUser.objects.filter(
            pk=request.user.id, role=CustomUser.Role.SELLER
        ).exists()


class IsOwner(BasePermission):
    """Разрешает действие только владельцу объекта"""

    def has_object_permission(self, request, view, obj):
        return obj.seller_id == request.user.id


__all__ = [IsModerator, IsOwner, IsSeller]
