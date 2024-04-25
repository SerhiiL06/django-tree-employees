from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from src.employees.models import Employee


class EmployeeListTestCase(TestCase):
    def setUp(self) -> None:

        User.objects.create_user(
            username="testUser", password="superSecurePassword"
        ).save()

        self.test_day = datetime.now().date()

        first = Employee.objects.create(
            first_name="test1",
            last_name="test1",
            middle_name="test1",
            email="test1",
            employment_at=self.test_day,
            position="position_1",
        )

        second = Employee.objects.create(
            first_name="test2",
            last_name="test2",
            middle_name="test2",
            email="test1@gmail.com",
            employment_at=self.test_day - timedelta(days=1),
            position="position_2",
            boss=first,
        )

        Employee.objects.create(
            first_name="test3",
            last_name="test3",
            middle_name="test3@gmail.com",
            email="test3@gmail.com",
            employment_at=self.test_day - timedelta(days=2),
            position="position_3",
            boss=second,
        )

    def test_get_employee_list(self):
        response = self.client.get("/list/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/list.html")
        self.assertEqual(len(response.context["object_list"]), 3)

    def test_get_employee_list_with_params(self):
        # test search
        response = self.client.get("/list/?search=test3")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/list.html")

        self.assertEqual(len(response.context["object_list"]), 1)

        # test date
        response = self.client.get(f"/list/?date={self.test_day}")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/list.html")

        self.assertEqual(len(response.context["object_list"]), 1)


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

    def test_delete_employee(self):
        # without auth request
        response = self.client.post("/list/3/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/list/3/delete/")

        self.client.login(username="testUser", password="superSecurePassword")

        # test get request
        response = self.client.get("/list/9/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")

        # test delete auth request
        response = self.client.post("/list/9/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")

        # check changed boss function
        self.assertTrue(Employee.objects.get(id=10).boss_id)

    def test_update_employee(self):
        # without auth request
        response = self.client.post("/list/10/update/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/list/10/update/")

        self.client.login(username="testUser", password="superSecurePassword")

        response = self.client.get("/list/19/update/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/update.html")

        # correct update
        update_id = 19
        referer = {"HTTP_REFERER": "/list/19/update/"}

        update_data = {
            "first_name": "test_new",
            "last_name": "test3",
            "middle_name": "test3",
            "email": "test2@gmail.com",
            "employment_at": datetime.now().date() - timedelta(days=2),
            "position": "position_4",
            "boss_id": 17,
        }
        response = self.client.post(
            f"/list/{update_id}/update/",
            update_data,
            **referer,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")
        self.assertEqual(Employee.objects.get(id=update_id).first_name, "test_new")
