from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from workers.parsing.main import parser_executer

from .forms import LogInForm, RegistrationForm


class SignUpView(FormView):
    template_name: str = "account/signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    success_message = "Successfully registered!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)


class LogInView(LoginView):
    template_name: str = "account/login.html"
    form_class = LogInForm
    success_url = reverse_lazy("home")
    redirect_authenticated_user = True
