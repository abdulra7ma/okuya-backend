# Generated by Django 4.1a1 on 2022-05-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_article_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="parsedsite",
            name="langauge",
            field=models.CharField(
                choices=[("en", "English"), ("ar", "Arabic"), ("ru", "Russain")],
                default=1,
                max_length=4,
            ),
            preserve_default=False,
        ),
    ]
