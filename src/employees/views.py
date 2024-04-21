from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.db.transaction import atomic
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from .forms import CreateAndUpdateEmployeeForm
from .logic import change_boss
from .models import Employee


class EmployeesTreeView(ListView):
    template_name = "employees/tree.html"
    model = Employee

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.GET.get("full"):
            object_list = self.get_queryset().filter(level__lt=9)
            return render(request, "employees/tree.html", {"object_list": object_list})

        object_list = self.get_queryset().filter(level__lt=2)
        return render(request, "employees/tree.html", {"object_list": object_list})


class EmployeeListView(ListView):
    template_name = "employees/list.html"
    model = Employee
    paginate_by = 50

    def get_queryset(self) -> QuerySet[Any]:
        query = Employee.objects.search(self.request.GET)
        return query


@method_decorator(login_required, name="dispatch")
class CreateEmployeeView(CreateView):
    template_name = "employees/create.html"
    model = Employee
    form_class = CreateAndUpdateEmployeeForm
    success_url = reverse_lazy("employees:list")

    @atomic
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = CreateAndUpdateEmployeeForm(request.POST)

        if form.is_valid():

            boss_instance = Employee.objects.select_for_update().filter(
                id=request.POST["boss_id"]
            )

            if boss_instance.first() and boss_instance.position < form.cleaned_data.get(
                "position"
            ):
                employee = form.save(commit=False)
                employee.boss = boss_instance.first()
                employee.save()
                return HttpResponseRedirect(reverse_lazy("employees:list"))

            return HttpResponseRedirect(request.META["HTTP_REFERER"])


@method_decorator(login_required, name="dispatch")
class UpdateEmployeeView(UpdateView):
    template_name = "employees/update.html"
    model = Employee
    form_class = CreateAndUpdateEmployeeForm
    success_url = reverse_lazy("employees:list")

    @atomic
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        current_empl = self.get_object()
        form = CreateAndUpdateEmployeeForm(instance=current_empl, data=request.POST)

        if form.is_valid():

            boss_id = form.cleaned_data.get("boss_id")
            employee = form.save(commit=False)

            if current_empl.boss_id != boss_id:

                boss_instance = Employee.objects.select_for_update().filter(id=boss_id)

                if (
                    boss_instance.first()
                    and boss_instance.position < form.cleaned_data.get("position")
                ):

                    employee.boss = boss_instance
                else:
                    return HttpResponseRedirect(request.META["HTTP_REFERER"])

            if form.has_changed("position"):
                change_boss(employee.id, employee.level)

            employee.save()

            return HttpResponseRedirect(reverse_lazy("employees:list"))

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


@method_decorator(login_required, name="dispatch")
class DeleteEmployeeView(DeleteView):
    template_name = "employees/list.html"
    model = Employee
    success_url = reverse_lazy("employees:list")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        employee_to_delete = self.get_object()
        change_boss(employee_to_delete.id, employee_to_delete.level)
        return super().post(request, *args, **kwargs)
