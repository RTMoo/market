from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Менеджер для создания пользователя и админа
    """

    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        role = role or CustomUser.Role.BUYER

        extra_fields["role"] = role
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.update(
            {
                "is_staff": True,
                "is_superuser": True,
                "role": CustomUser.Role.MODERATOR,
            }
        )

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя
    """

    class Role(models.TextChoices):
        BUYER = "B", "Покупатель"
        SELLER = "S", "Продавец"
        MODERATOR = "M", "Модератор"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=3, choices=Role.choices, default=Role.BUYER)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"
