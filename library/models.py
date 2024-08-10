from django.db import models

from users.models import User


class Author(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя автора")
    surname = models.CharField(max_length=250, verbose_name="Фамилия автора")
    second_name = models.CharField(max_length=250, verbose_name="Отчество автора", blank=True, null=True)
    country = models.CharField(max_length=250, verbose_name="Страна", blank=True, null=True)

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
    count = models.PositiveIntegerField(verbose_name="Количество книг", default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class LogService(models.Model):
    book = models.ManyToManyField(Book, verbose_name="Книги", related_name='book')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='user')
    date_the_book_was_taken = models.DateTimeField(default=None, blank=True, null=True,
                                                   verbose_name="Дата выдачи книги")
    date_when_the_book_was_returned = models.DateTimeField(default=None, blank=True, null=True,
                                                           verbose_name="Когда книгу нужно вернуть")
    book_return_date = models.DateTimeField(default=None, blank=True, null=True,
                                            verbose_name="Когда книга была возвращена")
