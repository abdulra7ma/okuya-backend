# Generated by Django 4.1a1 on 2022-05-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_rename_langauge_parsedsite_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="parsedsite",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]