# Generated by Django 4.2.6 on 2023-11-12 02:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="followers",
        ),
        migrations.RemoveField(
            model_name="user",
            name="followings",
        ),
    ]
