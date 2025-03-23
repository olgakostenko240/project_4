from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Продукт", help_text="Введите название продукта")
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта", blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="catalog/photo", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(help_text="Введите цену за продукт")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status_publication = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория продукта", help_text="Введите название категории продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории продукта",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
