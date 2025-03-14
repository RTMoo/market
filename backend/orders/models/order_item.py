from django.db.models import (
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    Model,
)


class OrderItem(Model):
    order = ForeignKey(to="orders.Order", on_delete=CASCADE, related_name="items")
    product = ForeignKey(to="products.Product", on_delete=CASCADE)
    seller = ForeignKey(to="accounts.CustomUser", on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order item {self.order}"
