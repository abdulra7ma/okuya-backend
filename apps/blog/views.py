from django.shortcuts import render
from django.views.generic import TemplateView
from workers.parsing.main import parser_executer


class HomePageView(TemplateView):
    template_name: str = "home.html"

    def get(self, request, *args, **kwargs):
        # parser_executer()
        return super().get(request, *args, **kwargs)