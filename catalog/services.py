from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from config.settings import CACHE_ENABLED

from .models import Category, Product


class ProductService:
    @staticmethod
    def get_products_by_category(category_id: int):
        """
        Возвращает QuerySet продуктов категории.
        Если категория не существует — выбрасывает ObjectDoesNotExist.
        """
        if not Category.objects.filter(id=category_id).exists():
            raise ObjectDoesNotExist("Категория не найдена")
        return Product.objects.filter(category_id=category_id).select_related('category')

def get_list_products_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products




