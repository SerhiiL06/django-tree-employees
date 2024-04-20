from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    template_name = "register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("employees:list")


class LoginUserView(LoginView):
    template_name = "login.html"
    model = User
    form_class = LoginForm
