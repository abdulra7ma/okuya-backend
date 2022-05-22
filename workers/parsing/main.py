from typing import List

import newspaper
from core import celery_app
from django.apps import apps
from newspaper import Article as NewsPaperArticle

# from django.template.defaultfilters import slugify
from slugify import slugify

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
    )
    article_obj.save()

    return True


def site_parser(urls: list):
    articles_list = []

    for url in urls:
        articles_list.append(NewsPaperArticle(url=url))

    return articles_list


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

        for sub_article in articles_cleaner(
            newspaper_site.articles[:num_of_articles_per_site]
        ):
            article = NewsPaperArticle(
                sub_article.url, memoize_articles=False, language=site.language
            )
            article.download()
            article.parse()
            article.nlp()

            if article.title != "" or article.text != "":
                articles.append(article)

        article_meta = {
            "articles": articles[:num_of_articles_per_site],
            "site": site,
        }
        articles_dict[site.name] = article_meta

    return articles_dict


# @celery_app.task(name="parser-executer")
def parser_executer():
    categories_articels_dict = articles_collector_by_category()

    for _, article_meta in categories_articels_dict.items():
        for article in article_meta["articles"]:
            article_parser(
                article, article_meta["site"], article_meta["site"].category
            )

    return "Parser has finished executing"
