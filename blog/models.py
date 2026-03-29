from django.db import models


class Blog(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    ]
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Название статьи")
    content = models.TextField(verbose_name="Контент", help_text="Контент статьи")
    image = models.ImageField(upload_to="blog/photo", verbose_name="Изображение", help_text="Изображение статьи")
    created_at = models.DateField(verbose_name="Дата создания", help_text="Дата создания статьи", blank=True, null=True)
    updated_at = models.DateField(verbose_name="Дата обновления", help_text="Дата обновления статьи", blank=True, null=True)
    publication_status = models.BooleanField(verbose_name="Статус публикации", help_text="Статус публикации статьи", default=False)
    views_counter = models.PositiveIntegerField(verbose_name="Количество просмотров", help_text="Количество просмотров статьи", default=0)
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
