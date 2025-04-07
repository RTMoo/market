import django_filters
from products.models import Product, Category

ALLOWED_FILTER_FIELDS = ['price_min', 'price_max', 'category']


class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', required=False)
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', required=False)
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Product
        fields = ALLOWED_FILTER_FIELDS
