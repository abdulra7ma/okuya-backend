from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms import Form

from .models import User


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(
        label="Enter First name",
        min_length=4,
        max_length=50,
        help_text="Required",
    )
    surname = forms.CharField(
        label="Enter Surname",
        min_length=4,
        max_length=50,
        help_text="Required",
    )
    email = forms.EmailField(
        max_length=100,
        help_text="Required",
        error_messages={"required": "Sorry, you will need an email"},
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "email",
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email can not be used.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Enter your name"}
        )
        self.fields["surname"].widget.attrs.update(
            {"placeholder": "Enter your surname"}
        )
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "Enter your email",
                "name": "email",
                "id": "id_email",
            }
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Enter a password"}
        )


class LogInForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your email",
                "id": "login-email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "id": "login-pwd",
            }
        )
    )


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your email",
                "id": "form-email",
            }
        ),
    )

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "id": "form-newpass",
            }
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "id": "form-new-pass2",
            }
        ),
    )
