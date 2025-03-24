from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    SET_NULL,
    DecimalField,
    DateTimeField,
)
from phonenumber_field.modelfields import PhoneNumberField


class Order(Model):
    buyer = ForeignKey(to="accounts.CustomUser", on_delete=SET_NULL, null=True)
    full_name = CharField(max_length=64)
    to_address = CharField(max_length=128)
    phone_number = PhoneNumberField()
    total_price = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        ordering = ["-created_at"]
