# Generated by Django 4.2.2 on 2024-08-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="token",
            field=models.TextField(default="", verbose_name="Токен"),
        ),
    ]
