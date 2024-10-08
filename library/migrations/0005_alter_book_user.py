# Generated by Django 5.0.7 on 2024-08-04 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_alter_book_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users_books",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Книга на руках у:",
            ),
        ),
    ]
