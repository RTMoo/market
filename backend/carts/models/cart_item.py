from django.db.models import Model, ForeignKey, CASCADE, PositiveIntegerField


class CartItem(Model):
    cart = ForeignKey(to="carts.Cart", on_delete=CASCADE, related_name="items")
    product = ForeignKey(to="products.Product", on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
