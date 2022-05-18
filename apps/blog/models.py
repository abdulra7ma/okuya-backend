import asyncio

# app imports
from account.mixins import DateTimeMixin
from django.db import models


class Category(DateTimeMixin):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return self.slug


class ParsedSite(DateTimeMixin):
    original_site = models.URLField()
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    logo_image = models.ImageField()

    class Meta:
        verbose_name = "Parsed Site"
        verbose_name_plural = "Parsed Sites"


# Create your models here.
class Article(DateTimeMixin):
    from_site = models.ForeignKey(
        ParsedSite, on_delete=models.SET_NULL, null=True
    )
    original_link = models.CharField(max_length=192)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(max_length=192)
    content = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return self.slug
