from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from products.models import Product, Category, Review
from products.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from commons.permissions import IsOwner, IsModerator, IsSeller
from commons.paginations import CustomPagination


class ProductViewSet(ModelViewSet):
    """
    Управление товарами.

    Доступ:
    - Просмотр — для всех.
    - Создание - только для аутентифицированных пользователей.
    - Изменение и удаление — только владельцы или модераторы.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        if self.action in ["create"]:
            return [IsAuthenticated(), IsSeller()]
        if self.action in ["partial_update", "update"]:
            return [IsAuthenticated(), IsOwner()]
        if self.action in ["destroy"]:
            return [IsAuthenticated(), (IsOwner | IsModerator)()]


class UserProductViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Товары текущего пользователя.

    Доступ:
    - Только для аутентифицированных пользователей.
    """

    serializer_class = ProductSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user.id)


class CategoryViewSet(ModelViewSet):
    """
    Управление категориями.

    Доступ:
    - Просмотр — для всех.
    - Создание, изменение и удаление — только модератор.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsModerator()]


class ReviewViewSet(ModelViewSet):
    """
    Управление отзывами.

    Доступ:
    - Просмотр — для всех.
    - Создание - только для аутентифицированных пользователей.
    - Изменение и удаление — только владельцы или модератор.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        if self.action in ["create"]:
            return [IsAuthenticated()]

        return [(IsOwner | IsModerator)()]
