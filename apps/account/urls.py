from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *


urlpatterns = [
    path('sigh-up/', RegisterView.as_view(), name='register'),
    path('login/', SighInView.as_view(), name='login'),
    path('logout', LogoutView.as_view(, name='logout')),
]