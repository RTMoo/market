from rest_framework.serializers import ModelSerializer, IntegerField
from reviews.models import Review


class ReviewSerializer(ModelSerializer):
    product_id = IntegerField()

    class Meta:
        model = Review
        fields = [
            "id",
            "buyer",
            "product_id",
            "comment",
            "rating",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "buyer", "created_at", "updated_at"]
