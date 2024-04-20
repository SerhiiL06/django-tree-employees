from .models import Employee


def change_boss(empl_id: int, level: int) -> None:
    new_boss = Employee.objects.filter(level=level).first()
    employees_to_update = Employee.objects.filter(boss_id=empl_id)

    for employee in employees_to_update:
        print(employee)
        print(employee.boss_id)
        print(new_boss.id)
        employee.boss_id = new_boss.id
        employee.save()
