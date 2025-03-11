from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from products.models import Category, Product
from profiles.models import Profile
from carts.models import Cart


class Command(BaseCommand):
    help = "Создает пользователя, категории и товары"

    def handle(self, *args, **kwargs):
        # Создаем суперпользователя
        if not CustomUser.objects.filter(email="admin@test.com").exists():
            user = CustomUser.objects.create_user(
                email="a@a.com", password="admin", role=CustomUser.Role.SELLER
            )
            Cart.objects.create(user=user)
            Profile.objects.create(user=user)
            self.stdout.write(
                self.style.SUCCESS(
                    "✅ Создан пользователь: email=a@a.com, password=admin"
                )
            )
        else:
            self.stdout.write(self.style.WARNING("⚠️ Пользователь уже существует"))

        # Создаем категории
        categories_data = [
            {"name": "Мобильник", "slug": "phone"},
            {"name": "Телевизор", "slug": "tv"},
            {"name": "Книга", "slug": "book"},
        ]
        categories = []
        for cat in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat["name"], slug=cat["slug"]
            )
            categories.append(category)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Создана категория: {cat['name']}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⚠️ Категория уже существует: {cat['name']}")
                )

        # Создаем продукты
        products_data = [
            {"name": "iPhone", "category": categories[0], "price": 50000},
            {"name": "LG", "category": categories[1], "price": 100000},
            {"name": "Книга по Python", "category": categories[2], "price": 2500},
        ]

        for product in products_data:
            prod, created = Product.objects.get_or_create(
                user=user,
                title=product["name"],
                category=product["category"],
                price=product["price"],
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Создан продукт: {product['name']}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⚠️ Продукт уже существует: {product['name']}")
                )

        self.stdout.write(self.style.SUCCESS("🎉 Данные успешно добавлены!"))
