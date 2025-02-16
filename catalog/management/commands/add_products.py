from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **options):
        category_1, _ = Category.objects.get_or_create(name="Роза", description="Большой выбор цветов")
        category_2, _ = Category.objects.get_or_create(name="Тюльпаны", description="Много сортов на любой выбор")

        products = [
            {"name": "Голандская", "description": "Очень красивая красная роза", "category": category_1, "price": 100},
            {"name": "Чайная", "description": "Очень красивая розовая роза", "category": category_1, "price": 70},
            {
                "name": "Принц Карнавал",
                "description": "Очень красивый тюльпан раннего цветения",
                "category": category_2,
                "price": 90,
            },
            {
                "name": "Оранж Принцесс",
                "description": "Махровый тюльпан раннего цветения",
                "category": category_2,
                "price": 110,
            },
            {
                "name": "Авиньон",
                "description": "Простой тюльпан позднего цветения",
                "category": category_2,
                "price": 80,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Продукт успешно добавлен: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт уже был добавлен: {product.name}"))
