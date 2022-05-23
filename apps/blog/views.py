from django.views.generic import DetailView, ListView
from workers.parsing.main import parser_executer

from blog.models import Article, Category


class HomePageView(ListView):
    template_name: str = "blog/home.html"
    context_object_name = "articles"
    queryset = Article.objects.all().order_by("-id")[:10]


class TrendingPageView(ListView):
    template_name: str = "blog/trending.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trending_titles_querysets = {}
        categories = Category.objects.all()

        for cat in categories:
            trending_titles_querysets[cat.name] = Article.objects.filter(
                category=cat
            )[:5]

        context["trending_titles"] = trending_titles_querysets

        return context


class ContentPageView(DetailView):
    template_name = "blog/content.html"
    slug_url_kwarg: str = "article_slug"
    slug_field: str = "slug"
    context_object_name: str = "article"
    model = Article

    def get_object(self):
        return Article.objects.filter(slug=self.kwargs["article_slug"]).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_paragraphs"] = self.get_object().content.split("\n")
        return context
