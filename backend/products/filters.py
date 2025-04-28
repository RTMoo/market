import django_filters
from products.models import Product, Category

ALLOWED_FILTER_FIELDS = ["price_min", "price_max", "category"]

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte", required=False
    )
    price_max = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte", required=False
    )
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), required=False
    )

    class Meta:
        model = Product
        fields = ALLOWED_FILTER_FIELDS

    def filter_queryset(self, queryset):
        # Получаем параметры фильтрации
        price_min = self.data.get('price_min')
        price_max = self.data.get('price_max')
        category = self.data.get('category')
        # Преобразуем строки в числа, если они есть
        if price_min:
            try:
                price_min = int(price_min[0])  # берем первое значение из списка
            except ValueError:
                price_min = None

        if price_max:
            try:
                price_max = int(price_max[0])  # берем первое значение из списка
            except ValueError:
                price_max = None

        # Преобразуем строку категорий в список чисел, если они есть
        if category:
            try:
                category = [int(cat) for cat in category[0].split(',')]  # split и преобразуем в список чисел
            except ValueError:
                category = []
        # Фильтрация на основе преобразованных значений
        if price_min and price_max:
            queryset = queryset.filter(price__gte=price_min, price__lte=price_max)
        elif price_max:
            queryset = queryset.filter(price__lte=price_max)
        elif price_min:
            queryset = queryset.filter(price__gte=price_min)

        # Фильтрация по категориям
        if category:
            queryset = queryset.filter(category__in=category)

        return queryset
