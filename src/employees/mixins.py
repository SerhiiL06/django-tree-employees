from django.db.models.query import QuerySet

from .models import Employee


class EmployeeMixin:
    def boss_changed(self, instance: QuerySet[Employee], new_position: str) -> bool:
        if instance.first() and instance.first().position < new_position:
            return True

    def is_changed(self, old: int, new: int) -> bool:
        return old != new

    def change_boss(self, empl_id: int, level: int) -> None:
        new_boss = Employee.objects.filter(level=level).first()
        employees_to_update = Employee.objects.filter(boss_id=empl_id)

        for employee in employees_to_update:
            employee.boss_id = new_boss.id
            employee.save()
