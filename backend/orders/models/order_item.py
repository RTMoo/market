from django.db.models import (
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    Model,
    TextChoices,
    CharField,
)


class OrderItem(Model):
    class Status(TextChoices):
        PENDING = "pending", "В обработке"
        PAID = "paid", "Оплачено"
        SHIPPED = "shipped", "Отправлено"
        DELIVERED = "delivered", "Доставлено"
        CANCELED = "canceled", "Отменено"

    order = ForeignKey(to="orders.Order", on_delete=CASCADE, related_name="items")
    product = ForeignKey(to="products.Product", on_delete=CASCADE)
    seller = ForeignKey(to="accounts.CustomUser", on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    status = CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"Order item {self.order}"
