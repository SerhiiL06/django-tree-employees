from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from mptt.forms import MoveNodeForm

from .forms import CreateEmployeeForm
from .models import Employee


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


@method_decorator(login_required, name="dispatch")
class CreateEmployeeView(CreateView):
    template_name = "create.html"
    model = Employee
    form_class = CreateEmployeeForm
    success_url = reverse_lazy("employees:list")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = CreateEmployeeForm(request.POST)

        if form.is_valid():
            boos_instance = Employee.objects.get(id=request.POST["boss_id"])
            if boos_instance.position < form.cleaned_data.get("position"):
                form.save()
                return HttpResponseRedirect(reverse_lazy("employees:list"))

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


@method_decorator(login_required, name="dispatch")
class UpdateEmployeeView(UpdateView):
    template_name = "update.html"
    model = Employee
    form_class = CreateEmployeeForm
    success_url = reverse_lazy("employees:list")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = CreateEmployeeForm(request.POST)

        if form.is_valid():
            boos_instance = Employee.objects.get(id=request.POST["boss_id"])
            if boos_instance.position < form.cleaned_data.get("position"):
                form.save()
                return HttpResponseRedirect(reverse_lazy("employees:list"))

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


@method_decorator(login_required, name="dispatch")
class DeleteEmployeeView(DeleteView):
    template_name = "list.html"
    model = Employee
    success_url = reverse_lazy("employees:list")
