# Generated by Django 4.1a1 on 2022-05-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_parsedsite_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="top_img",
            field=models.ImageField(blank=True, null=True, upload_to="article-img"),
        ),
    ]
