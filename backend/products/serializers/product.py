from rest_framework.serializers import ModelSerializer
from products.models import Product
from accounts.models import CustomUser


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "category",
            "created_at",
            "price",
            "stock",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        """
        Автоматическая привязка пользователя при создании продукта
        """

        user_id = self.context["request"].user.id
        user = CustomUser.objects.filter(pk=user_id).only("pk").first()
        validated_data["user"] = user
        return super().create(validated_data)
