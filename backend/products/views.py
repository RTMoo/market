from rest_framework.viewsets import ModelViewSet
from products.models import Product, Category, Review
from products.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from commons.permissions import IsOwner, IsModerator, IsReader


class ProductViewSet(ModelViewSet):
    """
    ViewSet для управления товароми

    - Доступ:
        - Читать могут все
        - Изменять, удалять могут только владельцы
    - queryset: все обьекты модели Product
    - serializer_class = ProductSerializer
    """

    permission_classes = [IsOwner | IsModerator | IsReader]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet для управления категориями

    - Доступ:
        - Только администраторы могут управлять категориями
    - queryset: Все объекты модели Category
    - serializer_class: CategorySerializer
    """

    permission_classes = [IsModerator | IsReader]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    """
    ViewSet для управления отзывами

    - Доступ:
        - Читать могут все
        - Изменять, удалять могут только владельцы
    - queryset: все обьекты модели Review
    - serializer_class = ReviewSerializer
    """

    permission_classes = [IsModerator | IsReader]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
