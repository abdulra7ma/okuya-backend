from django.db import models

# app imports
from account.mixins import DateTimeMixin


class Category(DateTimeMixin):
    name = models.CharField(max_length=128)


class ParsedSite(DateTimeMixin):
    original_site = models.URLField()
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    logo_image = models.ImageField()


# Create your models here.
class Blog(DateTimeMixin):
    from_site = models.ForeignKey(
        ParsedSite, on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(max_length=192)
    html_content = models.TextField()
