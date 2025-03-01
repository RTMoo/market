from django.db.models import Model, OneToOneField, CASCADE, CharField
from django.core.validators import MaxLengthValidator, MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField


class Profile(Model):
    user = OneToOneField(to="accounts.CustomUser", on_delete=CASCADE)
    first_name = CharField(
        max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(30)]
    )
    last_name = CharField(
        max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(30)]
    )
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
