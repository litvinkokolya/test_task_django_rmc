from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    date_of_birth = models.DateField(default=timezone.now, verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
