# Generated by Django 5.0.7 on 2024-08-10 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_book_return_date_user_date_the_book_was_taken_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="book_return_date",
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_the_book_was_taken",
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_when_the_book_was_returned",
        ),
    ]