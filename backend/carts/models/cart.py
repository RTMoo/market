from django.db.models import Model, ForeignKey, CASCADE


class Cart(Model):
    user = ForeignKey(to="accounts.CustomUser", on_delete=CASCADE, related_name="cart")
