from django.db.models import Model, CharField, SlugField


class Category(Model):
    name = CharField(max_length=255, unique=True)
    slug = SlugField(max_length=255, unique=True)
