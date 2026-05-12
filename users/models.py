from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Email пользователя")
    phone_number = models.CharField(max_length=10, verbose_name="Номер телефона", help_text="Номер телефона пользователя", blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatar", verbose_name="Аватар", help_text="Аватар пользователя", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Страна пользователя", blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name="Токен", help_text="Токен пользователя", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    

