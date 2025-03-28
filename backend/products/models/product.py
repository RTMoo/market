from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    PositiveIntegerField,
    DateTimeField,
    DecimalField,
    SET_NULL,
    ImageField,
)
from django.core.validators import MinValueValidator


class Product(Model):
    seller = ForeignKey(to="accounts.CustomUser", on_delete=SET_NULL, null=True)
    name = CharField(max_length=255)
    category = ForeignKey(
        to="products.Category", on_delete=SET_NULL, null=True, blank=True
    )
    description = CharField(max_length=512)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = DateTimeField(auto_now_add=True)
    image = ImageField(upload_to="products/", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
