from typing import Optional

from django.db.models.query import QuerySet

from .models import Employee


class EmployeeMixin:
    def correct_boss_id(self, instance: QuerySet[Employee], new_position: str) -> bool:
        if instance.first() and instance.first().position < new_position:
            return True

    def is_changed(self, old_id: int, new_id: Optional[int]) -> bool:

        return bool(new_id and old_id != new_id)

    def change_boss(self, empl_id: int, level: int) -> None:

        new_boss = Employee.objects.filter(level__lt=level).first()
        employees_to_update = Employee.objects.filter(boss_id=empl_id)

        for employee in employees_to_update:
            employee.boss = new_boss
            employee.save()
