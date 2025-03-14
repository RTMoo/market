from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from products.models import Category, Product
from profiles.models import Profile
from carts.models import Cart


class Command(BaseCommand):
    help = "Создает пользователя, категории и товары"

    def handle(self, *args, **kwargs):
        # Создаем продавца
        if not CustomUser.objects.filter(email="a@a.com").exists():
            seller = CustomUser.objects.create_user(
                email="a@a.com", password="admin", role=CustomUser.Role.SELLER
            )
            Cart.objects.create(user=seller)
            Profile.objects.create(user=seller)
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
            {
                "name": "iPhone",
                "category": categories[0],
                "price": 50000,
                "stock": 10,
                "description": "description",
            },
            {
                "name": "LG",
                "category": categories[1],
                "price": 100000,
                "stock": 2,
                "description": "description",
            },
            {
                "name": "Книга по Python",
                "category": categories[2],
                "price": 2500,
                "description": "description",
                "stock": 4,
            },
        ]

        for product in products_data:
            prod, created = Product.objects.get_or_create(
                seller=seller,
                title=product["name"],
                category=product["category"],
                price=product["price"],
                stock=product["stock"],
                description=product["description"],
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
