from django.contrib.auth.models import AbstractUser
from django.db import models

from library.models import Book


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Email')
    token = models.TextField(verbose_name='Токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
