from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
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

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()

        if self.request.GET.get("search"):
            search_text = self.request.GET.get("search")
            queryset = queryset.filter(
                Q(first_name__icontains=search_text)
                | Q(last_name__icontains=search_text)
                | Q(middle_name__icontains=search_text)
            )

        if self.request.GET.get("order"):
            order_fields = self.request.GET.get("order")
            queryset = queryset.order_by(order_fields)

        return queryset
