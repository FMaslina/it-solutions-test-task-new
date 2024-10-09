from django.contrib.auth import get_user_model
from django.db import models


class Car(models.Model):
    make = models.TextField(verbose_name="Марка")
    model = models.TextField(verbose_name="Модель")
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Создатель")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
