from django.conf import settings
from django.db import models


class Ad(models.Model):
    image = models.ImageField(
        upload_to='images/ad/'
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Название товара'
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    description = models.CharField(
        max_length=1500,
        blank=True,
        null=True,
        verbose_name='Описание товара'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания объявления',
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.CharField(
        max_length=1500,
        verbose_name='Комментарий'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )

    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявление'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время написания комментария'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ("-created_at",)
