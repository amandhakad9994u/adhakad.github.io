# Generated by Django 5.0.6 on 2024-05-21 03:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="register",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="register",
            name="last_name",
        ),
    ]
