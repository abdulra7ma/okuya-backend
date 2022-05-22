from django.views.generic import DetailView, ListView
from workers.parsing.main import parser_executer

from blog.models import Article


class HomePageView(ListView):
    template_name: str = "home.html"
    context_object_name = "articles"
    queryset = Article.objects.all().order_by("-id")[:10]

    def get(self, request, *args, **kwargs):
        # parser_executer()
        return super().get(request, *args, **kwargs)


class ContentPageView(DetailView):
    template_name = "content.html"
    slug_url_kwarg: str = "article_slug"
    slug_field: str = "slug"
    context_object_name: str = "article"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_paragraphs"] = self.get_object().content.split("\n")
        return context
