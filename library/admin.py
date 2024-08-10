from django.contrib import admin

from library.models import Author, Book, LogService


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'second_name', 'country']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'year_of_writen', 'publication_date']


@admin.register(LogService)
class LogServiceAdmin(admin.ModelAdmin):
    list_display = ['date_the_book_was_taken', 'date_when_the_book_was_returned', 'book_return_date']
