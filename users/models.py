from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Email', unique=True)
    token = models.TextField(null=True, blank=True, verbose_name='Токен')
    is_active = models.BooleanField(default=False, verbose_name='Активирован')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def update_return_date(self):
        if self.date_the_book_was_taken:
            self.date_when_the_book_was_returned = self.date_the_book_was_taken + timedelta(days=30)
            self.save(update_fields=['date_when_the_book_was_returned'])

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
