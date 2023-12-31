# Generated by Django 4.2.6 on 2023-10-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0003_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_details",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="user_details",
            name="phone",
            field=models.BigIntegerField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
