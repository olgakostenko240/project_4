from django.contrib import admin
from blogs.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "image", "views_counter")
    list_filter = ("title",)
    search_fields = ("title",)
