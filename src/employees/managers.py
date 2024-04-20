from datetime import datetime
from typing import TypeVar

from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet

T = TypeVar("T", str, None)


class EmployeeManager(models.Manager):

    def search(self, text: T, date: T, ordering: T) -> QuerySet[any]:
        queryset = self.get_queryset()
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

        return queryset
