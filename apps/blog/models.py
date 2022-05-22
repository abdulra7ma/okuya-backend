import asyncio

# app imports
from account.mixins import DateTimeMixin
from django.db import models
from django.template.defaultfilters import slugify


class Category(DateTimeMixin):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        app_label = "blog"

    def get_absolute_url(self):
        return self.slug

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ParsedSite(DateTimeMixin):
    SITE_LANGAUGE = [
        ("en", "English"),
        ("ar", "Arabic"),
        ("ru", "Russain"),
    ]
    original_site = models.URLField()
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    logo_image = models.ImageField(
        upload_to="site_logo", null=True, blank=True
    )
    language = models.CharField(max_length=4, choices=SITE_LANGAUGE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Parsed Site"
        verbose_name_plural = "Parsed Sites"

    def __str__(self) -> str:
        return self.name + ":" + str(self.original_site)

 
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
    slug = models.SlugField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def get_absolute_url(self):
        return self.slug

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
