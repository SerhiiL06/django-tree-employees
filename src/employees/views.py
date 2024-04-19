from typing import Any
from django.db.models.query import QuerySet
from .models import Employee
from django.views.generic import ListView


class EmployeesTreeView(ListView):
    template_name = "tree.html"
    model = Employee

    def get_queryset(self) -> QuerySet[Any]:
        return Employee.objects.filter(level__lte=2)


class EmployeeListView(ListView):
    template_name = "list.html"
    model = Employee
    paginate_by = 50
