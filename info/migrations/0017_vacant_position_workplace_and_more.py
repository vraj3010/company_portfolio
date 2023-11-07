# Generated by Django 4.2.6 on 2023-11-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0016_remove_vacant_position_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacant_position",
            name="workplace",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="vacant_position",
            name="company_description",
            field=models.TextField(
                help_text="Enter Description about Company", max_length=2000, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vacant_position",
            name="role_description",
            field=models.TextField(
                help_text="Enter description about Role..", max_length=2000, null=True
            ),
        ),
    ]
