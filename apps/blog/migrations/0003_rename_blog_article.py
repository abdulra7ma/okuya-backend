# Generated by Django 4.1a1 on 2022-05-18 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_html_content_blog_content_blog_original_link"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Blog",
            new_name="Article",
        ),
    ]