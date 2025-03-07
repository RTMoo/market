from rest_framework.serializers import ModelSerializer
from products.models import Product
from accounts.models import CustomUser


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "user",
            "title",
            "description",
            "category",
            "created_at",
            "price",
            "stock",
        ]
        read_only_fields = ["id", "created_at", "user"]

    def create(self, validated_data):
        """
        Автоматическая привязка пользователя при создании продукта
        """

        user_id = self.context["request"].user.id
        user = CustomUser.objects.only("pk").get(pk=user_id)
        validated_data["user"] = user
        return super().create(validated_data)
