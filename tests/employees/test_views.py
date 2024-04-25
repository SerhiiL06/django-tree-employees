from django.test import TestCase
from src.employees.models import Employee
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse


class EmployeeListTestCase(TestCase):
    def setUp(self) -> None:

        User.objects.create_user(
            username="testUser", password="superSecurePassword"
        ).save()

        first = Employee.objects.create(
            first_name="test1",
            last_name="test1",
            middle_name="test1",
            email="test1",
            employment_at=datetime.now().date(),
            position="position_1",
        )

        second = Employee.objects.create(
            first_name="test1",
            last_name="test1",
            middle_name="test1",
            email="test1",
            employment_at=datetime.now().date() - timedelta(days=1),
            position="position_2",
            boss=first,
        )

        Employee.objects.create(
            first_name="test1",
            last_name="test1",
            middle_name="test1",
            email="test1",
            employment_at=datetime.now().date() - timedelta(days=2),
            position="position_3",
            boss=second,
        )

        self.test_day = datetime.now().date() - timedelta(days=1)

    def test_get_employee_list(self):
        response = self.client.get("/list/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/list.html")
        self.assertEqual(len(response.context["object_list"]), 3)


class EmployeeActionsTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username="testUser", password="superSecurePassword"
        ).save()

        first = Employee.objects.create(
            first_name="test1",
            last_name="test1",
            middle_name="test1",
            email="test1",
            employment_at=datetime.now().date(),
            position="position_1",
        )

        second = Employee.objects.create(
            first_name="test2",
            last_name="test2",
            middle_name="test2",
            email="test2",
            employment_at=datetime.now().date() - timedelta(days=1),
            position="position_2",
            boss=first,
        )

        Employee.objects.create(
            first_name="test3",
            last_name="test3",
            middle_name="test3",
            email="test2",
            employment_at=datetime.now().date() - timedelta(days=2),
            position="position_3",
            boss=second,
        )

    def test_get_empl_creating_view_without_auth(self):

        response = self.client.get(reverse("employees:create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/create/")

    def test_get_empl_creating_view(self):
        self.client.login(username="testUser", password="superSecurePassword")

        response = self.client.get(reverse("employees:create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/create.html")
        self.assertTrue(response.context["form"])

    def test_create_employee(self):

        data_to_save = {
            "first_name": "test10",
            "last_name": "test10",
            "middle_name": "test10",
            "email": "test10@gmail.com",
            "employment_at": datetime.now().date(),
            "position": "position_5",
            "boss_id": 1,
        }

        self.client.login(username="testUser", password="superSecurePassword")

        response = self.client.post("/create/", data=data_to_save)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")

        self.assertEqual(Employee.objects.count(), 4)

    def test_create_employee_with_equal_boss(self):
        data_to_save = {
            "first_name": "test10",
            "last_name": "test10",
            "middle_name": "test10",
            "email": "test10@gmail.com",
            "employment_at": datetime.now().date(),
            "position": "position_1",
            "boss_id": 1,
        }

        self.client.login(username="testUser", password="superSecurePassword")

        response = self.client.post("/create/", data=data_to_save)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, "/create/")
