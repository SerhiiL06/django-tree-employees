from django.db.models.query import QuerySet

from .models import Employee


class EmployeeMixin:
    def correct_boss_id(self, instance: QuerySet[Employee], new_position: str) -> bool:
        if instance.first() and instance.first().position < new_position:
            return True

    def is_changed(self, old: int, new: int | None) -> bool:

        return bool(new and old != new)

    def change_boss(self, empl_id: int, level: int) -> None:

        new_boss = Employee.objects.filter(level__lt=level).first()
        employees_to_update = Employee.objects.filter(boss_id=empl_id)

        for employee in employees_to_update:
            employee.boss = new_boss
            employee.save()
