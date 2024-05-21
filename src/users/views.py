from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm


class RegisterView(CreateView):
    template_name = "users/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("employees:list")

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:

        if request.user.is_authenticated:
            return redirect("employees:list")
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Success register")
            return redirect("employees:list")

        errors = list(form.error_messages.values())

        return render(request, self.get_template_names(), {"error_list": errors})


class LoginUserView(LoginView):
    template_name = "users/login.html"
    model = User
    form_class = LoginForm

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("employees:list")
        return super().get(request, *args, **kwargs)
