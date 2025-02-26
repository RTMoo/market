from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "user", "title", "description", "category", "created_at"]
        read_only_fields = ["id", "user", "created_at"]

    def create(self, validated_data):
        """
        Автоматическая привязка пользователя при создании продукта
        """

        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)
