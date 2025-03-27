from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from rest_framework.exceptions import PermissionDenied
from reviews.models import Review
from accounts.models import CustomUser
from products.models import Product
from orders.models import OrderItem

class ReviewSerializer(ModelSerializer):
    product = PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = [
            "id",
            "buyer",
            "product",
            "comment",
            "rating",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "buyer", "created_at", "updated_at"]

    def validate(self, data):
        """
        Запрет на повторные отзывы от одного клиента к одному товару
        """

        buyer_id = self.context["request"].user.id
        buyer: CustomUser = CustomUser.objects.filter(id=buyer_id).first()
        product: Product = data.get("product")

        if not OrderItem.objects.select_related("order").filter(order__buyer_id=buyer_id).exists():
            raise PermissionDenied("Оставить отзыв можно только после покупки данного товара")
        
        if Review.objects.filter(buyer=buyer, product=product).exists():
            raise PermissionDenied("Вы уже оставили отзыв на этот товар.")

        data["buyer"] = buyer
        return data
