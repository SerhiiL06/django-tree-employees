from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.EmployeeListView.as_view()),
    path("tree/", views.EmployeesTreeView.as_view()),
]
