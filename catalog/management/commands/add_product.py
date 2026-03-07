from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command


class Command(BaseCommand):
    help = "Создает категории и продуктов через фикстуры"

    def handle(self, *args, **kwargs):
        """Создает категории и продукты"""
        self.stdout.write(self.style.SUCCESS("Создание категорий и продуктов"))
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Категории и продукты удалены"))

        call_command("loaddata", "category_fixture.json")
        call_command("loaddata", "product_fixture.json")

        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены"))
