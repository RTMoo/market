from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "seller",
            "name",
            "description",
            "category",
            "created_at",
            "price",
            "stock",
            "image",
        ]
        read_only_fields = ["id", "created_at", "seller"]
