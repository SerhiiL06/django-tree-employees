from datetime import datetime

from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet


class EmployeeManager(models.Manager):

    def search(self, params: dict) -> QuerySet[any]:
        queryset = self.get_queryset()
        text = params.get("search")
        date = params.get("date")
        ordering = params.get("order")

        if text:
            queryset = queryset.filter(
                Q(first_name__icontains=text)
                | Q(last_name__icontains=text)
                | Q(middle_name__icontains=text)
            )
        if date:
            d = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = queryset.filter(employment_at=d)

        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by("last_name")

        return queryset
