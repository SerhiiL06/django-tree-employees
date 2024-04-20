from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [
    path("create/", views.CreateEmployeeView.as_view(), name="create"),
    path("list/", views.EmployeeListView.as_view(), name="list"),
    path("tree/", views.EmployeesTreeView.as_view(), name="tree"),
    path("list/<int:pk>/delete/", views.DeleteEmployeeView.as_view(), name="delete"),
    path("list/<int:pk>/update/", views.UpdateEmployeeView.as_view(), name="update"),
]
