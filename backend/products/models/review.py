from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    DateTimeField,
    IntegerField,
)
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(Model):
    product = ForeignKey(
        to="products.Product",
        on_delete=CASCADE,
        related_name="product_reviews"
    )
    user = ForeignKey(
        to="accounts.CustomUser",
        on_delete=CASCADE,
        related_name="user_reviews"
    )
    rating = IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = CharField(
        max_length=255,
        blank=True,
        null=True
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
