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
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Название товара"
    )
    description = models.TextField(
        max_length=1000, verbose_name="Описание", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Выберите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        blank=True,
        null=True,
        help_text="Выберите категорию",
    )
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(blank=True, null=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category"]

    def __str__(self):
        return self.name
