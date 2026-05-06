from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Название категории"
    )
    description = models.TextField(
        max_length=1000,
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Название товара"
    )
    description = models.TextField(
        max_length=1000, verbose_name="Описание", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Выберите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="catalog",
        blank=True,
        null=True,
        help_text="Выберите категорию",
    )
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Количество просмотров",
        default=0,
    )
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(blank=True, null=True, verbose_name="Дата обновления")
    publication_status = models.BooleanField(verbose_name="Статус публикации", help_text="Статус публикации продукта", default=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name
