# from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User
from .forms import RegistrationForm
# Create your views here.


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    success_message = 'Successfully registered!'


class SighInView(LoginView):
    template_name = 'login.html'

# from django.shortcuts import render, redirect
# from .forms import RegisterForm


# Create your views here.
# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/home")
#     else:
#         form = RegisterForm()
#
#     return render(response, "signup-page.html", {"form": form})

