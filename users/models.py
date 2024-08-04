from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Email', unique=True)
    token = models.TextField(null=True, blank=True, verbose_name='Токен')
    is_active = models.BooleanField(default=False, verbose_name='Активирован')
    date_the_book_was_taken = models.DateTimeField(default=None, blank=True, null=True,
                                                   verbose_name="Дата выдачи книги")
    date_when_the_book_was_returned = models.DateTimeField(default=None, blank=True, null=True,
                                                           verbose_name="Дата возврата книги")
    book_return_date = models.DateTimeField(default=None, blank=True, null=True, verbose_name="Дата возврата книги")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
