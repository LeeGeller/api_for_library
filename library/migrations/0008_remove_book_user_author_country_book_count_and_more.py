# Generated by Django 5.0.7 on 2024-08-10 12:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0007_alter_book_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="user",
        ),
        migrations.AddField(
            model_name="author",
            name="country",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Страна"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="count",
            field=models.PositiveIntegerField(
                default=1, verbose_name="Количество книг"
            ),
        ),
        migrations.CreateModel(
            name="LogService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_the_book_was_taken",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Дата выдачи книги"
                    ),
                ),
                (
                    "date_when_the_book_was_returned",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Когда книгу нужно вернуть",
                    ),
                ),
                (
                    "book_return_date",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Когда книга была возвращена",
                    ),
                ),
                (
                    "book_on_user",
                    models.BooleanField(
                        default=True, verbose_name="Книга на руках у пользователя"
                    ),
                ),
                (
                    "book",
                    models.ManyToManyField(
                        related_name="book", to="library.book", verbose_name="Книги"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
    ]
