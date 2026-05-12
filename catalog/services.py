from .models import Category, Product


class ProductService:
    @staticmethod
    def product_in_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
            return Product.objects.filter(category=category)
        except Category.DoesNotExist:
            return None








