# Generated by Django 5.0.7 on 2024-08-04 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_alter_book_book_return_date_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default="Нет книг на руках",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Книга на руках у:",
            ),
        ),
    ]
