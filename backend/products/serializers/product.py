from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    SerializerMethodField,
)
from products.models import Product


class ProductSerializer(ModelSerializer):
    category_id = IntegerField(write_only=True)
    category_name = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "seller",
            "name",
            "description",
            "category_id",
            "category_name",
            "created_at",
            "price",
            "stock",
            "image",
        ]
        read_only_fields = ["id", "created_at", "seller", "category_name"]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else "Без категории"
