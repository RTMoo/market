from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    FloatField,
    PositiveIntegerField,
    DateTimeField,
    SET_NULL,
)


class Product(Model):
    user = ForeignKey(to="accounts.CustomUser", on_delete=SET_NULL, null=True)
    title = CharField(max_length=255)
    category = ForeignKey(
        to="products.Category", on_delete=SET_NULL, null=True, blank=True
    )
    description = CharField(max_length=512)
    price = FloatField(default=0)
    stock = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)
