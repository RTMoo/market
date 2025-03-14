from django.db.models import (
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    DecimalField,
    Model,
)


class OrderItem(Model):
    order = ForeignKey(to="orders.Order", on_delete=CASCADE, related_name="items")
    product = ForeignKey(to="product.Product", on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order item {self.order}"
