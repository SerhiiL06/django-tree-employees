from datetime import datetime

from django.test import TestCase

from src.employees.forms import CreateAndUpdateEmployeeForm


class FormTestCase(TestCase):
    def test_creating_form(self):
        data_to_save = {
            "first_name": "test10",
            "last_name": "test10",
            "middle_name": "test10",
            "email": "test10@gmail.com",
            "employment_at": datetime.now().date(),
            "position": "position_5",
            "boss_id": 1,
        }

        form = CreateAndUpdateEmployeeForm(data=data_to_save)

        self.assertTrue(form.is_valid())
