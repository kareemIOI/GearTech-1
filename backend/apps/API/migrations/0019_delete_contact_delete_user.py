# Generated by Django 4.1.7 on 2023-04-21 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0018_user_gender_user_status"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]