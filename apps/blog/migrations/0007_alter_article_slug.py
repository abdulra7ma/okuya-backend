# Generated by Django 4.1a1 on 2022-05-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_category_options_alter_parsedsite_logo_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(),
        ),
    ]
