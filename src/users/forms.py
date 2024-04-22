from typing import Any
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self) -> dict[str, Any]:
        clean = super().clean()

        if clean.get("password1") != clean.get("password2"):
            raise ValidationError("Passwords must be the same")

        return clean


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
