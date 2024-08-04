from django.db import models

from users.models import User


class Author(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя автора")
    surname = models.CharField(max_length=250, verbose_name="Фамилия автора")
    second_name = models.CharField(max_length=250, verbose_name="Отчество автора", blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname} {self.second_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.TextField(verbose_name="Название книги")
    author = models.ManyToManyField(Author, verbose_name="Автор книги", related_name='author')
    genre = models.TextField(verbose_name="Жанр книги")
    year_of_writen = models.PositiveIntegerField(verbose_name="Год написания книги")
    publication_date = models.PositiveIntegerField(verbose_name="Год издания книги")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Книга на руках у:",
                             related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
