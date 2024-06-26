from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
