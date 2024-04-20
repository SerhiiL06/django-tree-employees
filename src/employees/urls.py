from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [
    path("list/", views.EmployeeListView.as_view(), name="list"),
    path("tree/", views.EmployeesTreeView.as_view()),
]
