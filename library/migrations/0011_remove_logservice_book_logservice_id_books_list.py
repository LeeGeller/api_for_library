# Generated by Django 4.2.2 on 2024-08-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0010_remove_logservice_book_logservice_id_books_list_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logservice",
            name="book",
        ),
        migrations.AddField(
            model_name="logservice",
            name="id_books_list",
            field=models.ManyToManyField(
                related_name="id_books_list", to="library.book", verbose_name="Книги"
            ),
        ),
    ]
