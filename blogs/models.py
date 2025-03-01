from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите название заголовка")
    content = models.TextField(verbose_name="Описание статьи", help_text="Введите текст статьи", blank=True, null=True)
    image = models.ImageField(
        upload_to="blogs/image", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото для статьи"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    publication_sign = models.BooleanField(default=True, verbose_name="Публикация")
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", help_text="Укажите количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"
        ordering = ["title"]

    def __str__(self):
        return self.title
