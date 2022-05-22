from django.contrib import admin

from .models import Article, Category, ParsedSite

admin.site.register(ParsedSite)
admin.site.register(Article)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
