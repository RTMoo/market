from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    PositiveIntegerField,
    DateTimeField,
    DecimalField,
    SET_NULL,
)


class Product(Model):
    user = ForeignKey(
        to="accounts.CustomUser",
        on_delete=SET_NULL,
        null=True,
        related_name="user_products",
    )
    title = CharField(max_length=255)
    category = ForeignKey(
        to="products.Category", on_delete=SET_NULL, null=True, blank=True
    )
    description = CharField(max_length=512)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)
