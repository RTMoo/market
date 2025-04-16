from django.db.models import Model, ForeignKey, CASCADE


class Cart(Model):
    buyer = ForeignKey(to="accounts.CustomUser", on_delete=CASCADE, related_name="cart")
