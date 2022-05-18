# Generated by Django 4.1a1 on 2022-05-18 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_rename_blog_article"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="parsedsite",
            options={
                "verbose_name": "Parsed Site",
                "verbose_name_plural": "Parsed Sites",
            },
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]