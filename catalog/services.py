from django.core.cache import cache
from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_catalog_from_cache():
    """Получает данные из кэша, если кэш пуст, получает данные из бд."""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class ProductService:

    @classmethod
    def get_product(cls):
        """Получаем все продукты"""
        products = Product.objects.all()
        return products

    @classmethod
    def get_product_by_id(cls, products_id):
        """Получаем продукты по id"""
        product_id = Product.objects.get(id=products_id)
        return product_id

    @classmethod
    def get_published_products(cls):
        """Получаем продукты которые опубликованны на сайте"""
        return Product.objects.filter(status_publication=True)

    @classmethod
    def get_product_name(cls, name):
        """Получаем название продуктов"""
        return Product.objects.get(name=name)

    @classmethod
    def get_published_products_by_name(cls, name):
        """Получаем название продуктов которые опубликованны на сайте"""
        published_name = Product.objects.filter(name=name, status_publication=True)
        return published_name

    @classmethod
    def get_published_products_by_category(cls, category_name):
        """Фильтруем продукты по категориям"""
        products = Product.objects.filter(category__name=category_name)
        return products
