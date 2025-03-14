from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    SET_NULL,
    DecimalField,
    DateTimeField,
    TextChoices,
)
from phonenumber_field.modelfields import PhoneNumberField


class Order(Model):
    class Status(TextChoices):
        PENDING = "pending", "В обработке"
        PAID = "paid", "Оплачено"
        SHIPPED = "shipped", "Отправлено"
        DELIVERED = "delivered", "Доставлено"
        CANCELED = "canceled", "Отменено"

    buyer = ForeignKey(to="accounts.CustomUser", on_delete=SET_NULL, null=True)
    full_name = CharField(max_length=64)
    to_address = CharField(max_length=128)
    phone_number = PhoneNumberField()
    status = CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total_price = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
