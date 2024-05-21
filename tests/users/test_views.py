from django.contrib.auth.models import User
from django.test import TestCase


class RegisterTestCase(TestCase):

    def test_get_register(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_post_register(self):

        user_data = {
            "username": "test",
            "email": "userTest@gmail.com",
            "password1": "TestPassword11",
            "password2": "TestPassword11",
        }

        response = self.client.post(
            "/register/",
            data=user_data,
        )
        users = User.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")

        self.assertEqual(len(users), 1)

        user_data["password2"] = "TestPassword12"

        wrong_response = self.client.post(
            "/register/",
            data=user_data,
        )

        self.assertEqual(wrong_response.status_code, 200)
        self.assertEqual(len(users), 1)

        form = wrong_response.context["form"]

        self.assertEqual(len(form.errors), 3)


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            "testUser", "testUser@gmail.com", "theSecretPassword"
        ).save()

    def test_get_login(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertTrue(response.context.get("form"))

    def test_get_login_auth_user(self):
        self.client.login(username="testUser", password="theSecretPassword")
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/list/")
