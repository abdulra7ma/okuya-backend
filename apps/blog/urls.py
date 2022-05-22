from django.urls import path
from .views import HomePageView, ContentPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path(
        "article/<slug:article_slug>",
        ContentPageView.as_view(),
        name="content-page",
    ),
]
