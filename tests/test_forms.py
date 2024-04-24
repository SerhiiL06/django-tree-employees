from django.test import TestCase
from src.users.forms import RegisterForm


class TestUsersForm(TestCase):
    def test_register_form(self):
        user_data = {
            "username": "test",
            "email": "userTest@gmail.com",
            "password1": "TestPassword11",
            "password2": "TestPassword11",
        }

        form = RegisterForm(data=user_data)

        self.assertTrue(form.is_valid())

        user_data["password2"] = "TestPassword12"

        wrong_form = RegisterForm(data=user_data)

        self.assertFalse(wrong_form.is_valid())

        password_error = wrong_form.errors.get("password2")

        self.assertTrue(bool(password_error))
        self.assertEqual(password_error[0], "The two password fields didn’t match.")
