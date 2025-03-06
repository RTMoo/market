from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from products.models import Product, Category, Review
from products.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from commons.permissions import IsOwner, IsModerator, IsReader, IsAuthenticated
from commons.paginations import CustomPagination


class ProductViewSet(ModelViewSet):
    """
    Управление товарами.

    Доступ:
    - Просмотр — для всех.
    - Изменение и удаление — только владельцы.

    Используется пагинация.
    """

    permission_classes = [IsReader | IsOwner | IsModerator]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


class UserProductViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Товары текущего пользователя.

    Доступ:
    - Только для аутентифицированных пользователей.

    """

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user.id)


class CategoryViewSet(ModelViewSet):
    """
    Управление категориями.

    Доступ:
    - Просмотр — для всех.
    - Изменение и удаление — только модератор.
    """

    permission_classes = [IsReader | IsModerator]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    """
    Управление отзывами.

    Доступ:
    - Просмотр — для всех.
    - Изменение и удаление — только владельцы или модератор.
    """

    permission_classes = [IsReader | IsOwner | IsModerator]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
