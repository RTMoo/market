from rest_framework.serializers import ModelSerializer, ValidationError
from products.models import Product
from accounts.models import CustomUser


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "seller",
            "title",
            "description",
            "category",
            "created_at",
            "price",
            "stock",
            "image",
        ]
        read_only_fields = ["id", "created_at", "seller"]

    def create(self, validated_data):
        """
        Автоматическая привязка пользователя при создании продукта
        """

        user_id = self.context["request"].user.id
        seller = CustomUser.objects.filter(pk=user_id).first()

        if not seller:
            raise ValidationError

        validated_data["seller"] = seller
        return super().create(validated_data)
