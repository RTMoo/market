from rest_framework.viewsets import ModelViewSet, GenericViewSet
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import BasePermission, AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.mixins import ListModelMixin



class IsAdminPermission(BasePermission):
    """
    Разрешение, которое проверяет, является ли пользователь админом (is_staff=True).
    """

    def has_permission(self, request, view):
        access_token = request.auth
        if not access_token:
            return False

        token = AccessToken(str(request.auth))
        return token.get("is_staff", False)


class ProductListView(ListModelMixin, GenericViewSet):
    """
    ViewSet для чтения списка товаров.

    - Доступ: 
        - Все пользователи.
    - queryset: Все объекты модели Product.
    - serializer_class: ProductSerializer.
    """
    
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    """
    ViewSet для управления категориями.

    - Доступ:
        - Только администраторы могут управлять категориями.
    - queryset: Все объекты модели Category.
    - serializer_class: CategorySerializer.
    """

    permission_classes = [IsAdminPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
