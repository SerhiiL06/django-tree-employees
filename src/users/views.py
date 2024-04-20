from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = "register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("employees:list")
