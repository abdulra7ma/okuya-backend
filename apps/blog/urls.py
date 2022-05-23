from django.urls import path
from .views import HomePageView, ContentPageView, TrendingPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "article/<slug:article_slug>",
        ContentPageView.as_view(),
        name="content",
    ),
    path("trending", TrendingPageView.as_view(), name="trending"),
]
