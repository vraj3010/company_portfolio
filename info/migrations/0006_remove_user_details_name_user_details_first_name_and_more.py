# Generated by Django 4.2.6 on 2023-10-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0005_alter_user_details_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_details",
            name="name",
        ),
        migrations.AddField(
            model_name="user_details",
            name="first_name",
            field=models.CharField(
                help_text="Enter your first name", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="user_details",
            name="last_name",
            field=models.CharField(
                help_text="Enter your first name", max_length=100, null=True
            ),
        ),
    ]
