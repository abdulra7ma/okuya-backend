from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .forms import PwdResetConfirmForm, PwdResetForm
from .views import LogInView, SignUpView

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", LogInView.as_view(), name="login"),
    path(
        "logout",
        LogoutView.as_view(next_page="/login"),
        name="logout",
    ),
    # password rest
    path(
        "password_reset",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset/password_reset_form.html",
            success_url="password_reset_email_confirm",
            email_template_name="account/password_reset/password_reset_email.html",
            form_class=PwdResetForm,
        ),
        name="pwdreset",
    ),
    path(
        "password_reset_email_confirm",
        TemplateView.as_view(
            template_name="account/password_reset/reset_status.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset/password_reset_confirm.html",
            success_url="password_reset_complete",
            form_class=PwdResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete",
        TemplateView.as_view(
            template_name="account/password_reset/reset_status.html"
        ),
        name="password_reset_complete",
    ),
]
