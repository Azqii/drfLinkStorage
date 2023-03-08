from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Link(models.Model):
    """Link model"""
    added_by = models.ForeignKey(
        to=AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Добавил", related_name="links"
    )
    link_url = models.TextField(blank=False, verbose_name="Ссылка")
    description = models.TextField(blank=False, verbose_name="Описание")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
