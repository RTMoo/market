from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Разрешение, которое проверяет, является ли пользователь админом (is_staff=True).
    """

    def has_permission(self, request, view):
        access_token = request.auth
        if not access_token:
            return False

        token = AccessToken(str(request.auth))
        return token.get("is_staff", False)


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает изменение объекта только владельцу, но позволяет всем читать.
    """

    def has_object_permission(self, request, view, obj):
        # Если метод для чтение
        if request.method in SAFE_METHODS:
            return True

        # Пользователь и есть создатель
        return obj.user == request.user
