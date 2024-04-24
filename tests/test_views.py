from django.test import TestCase
from django.contrib.auth.models import User


class MainTest(TestCase):

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
