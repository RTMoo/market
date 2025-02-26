from rest_framework.serializers import ModelSerializer, ValidationError
from products.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "product",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def create(self, validated_data):
        """
        Автоматическая привязка пользователя при создании отзыва
        """

        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)

    def validate(self, data):
        """
        Запрет на повторные отзывы от одного клиента к одному товару
        """

        user = self.context["request"].user
        product = data.get("product")

        if Review.objects.filter(user=user, product=product).exists():
            raise ValidationError("Вы уже оставили отзыв на этот товар.")

        return data
