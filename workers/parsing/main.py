from typing import List

import newspaper
from core import celery_app
from django.apps import apps
from newspaper import Article as NewsPaperArticle

# from django.template.defaultfilters import slugify
from slugify import slugify
from .site_beatifiers import bbc_beatify_article_text, download_image

from bs4 import BeautifulSoup

Category = apps.get_model("blog.Category")
ParsedSite = apps.get_model("blog.ParsedSite")
Article = apps.get_model("blog.Article")


def article_parser(
    article: NewsPaperArticle,
    from_site: ParsedSite,
    category: Category,
):
    """
    Takes an Aricle object and saves the needed information
    inside the db
    """

    article_obj: Article = Article.objects.create(
        from_site=from_site,
        original_link=article.url,
        category=category,
        title=article.title,
        content=article.text,
        slug=slugify(article.title, allow_unicode=True),
        top_img=article.top_image
    )
    article_obj.save()

    return True


def articles_cleaner(articles: List[NewsPaperArticle]):
    """
    Remove contentless article object
    """
    cleaned_articles = []

    for article in articles:
        if not (
            article.title == ""
            or article.title == "0"
            or article.title == None
            or "#" in article.url
        ):
            cleaned_articles.append(article)
    return cleaned_articles


def articles_collector_by_category():
    """
    Requests site related category and maps the site's articles
    to a dict key with the name of the category.
    """
    articles_dict = {}
    parsed_sites = ParsedSite.objects.filter(is_active=True)

    for site in parsed_sites:
        newspaper_site = newspaper.build(
            site.original_site, memoize_articles=False, language=site.language
        )
        # declares the number of articles to be pulled from one site
        # the default number is 9 articles per site
        num_of_articles_per_site = (
            9
            if len(newspaper_site.articles) > 9
            else len(newspaper_site.articles)
        )

        articles: List[NewsPaperArticle] = []

        for sub_article in articles_cleaner(newspaper_site.articles)[
            :num_of_articles_per_site
        ]:
            article = NewsPaperArticle(
                sub_article.url, memoize_articles=False, language=site.language
            )
            article.download()
            article.parse()
            article.nlp()

            # don't append the article if the article has no content
            if article.text != "":
                articles.append(article)

        articles = [
            bbc_beatify_article_text(article)
            if "bbc" in article.url
            else article
            for article in articles
        ][:num_of_articles_per_site]

        # download article top image and change the attribute value
        # of article' top_img to the new local static image
        for artc in articles:
            artc.top_image = download_image(artc.top_image)

        article_meta = {
            "articles": articles,
            "site": site,
        }
        articles_dict[site.name] = article_meta

    return articles_dict


def parser_executer():
    categories_articels_dict = articles_collector_by_category()

    for _, article_meta in categories_articels_dict.items():
        for article in article_meta["articles"]:
            article_parser(
                article, article_meta["site"], article_meta["site"].category
            )

    return "Parser has finished executing"
