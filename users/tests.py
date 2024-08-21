from http import HTTPStatus as status
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import User, EmailVerification


class RegistrationUserViewTest(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test_user',
            'email': 'test@test.test',
            'password1': 'password_1',
            'password2': 'password_1',
        }

    def test_registration_user_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, status.OK)
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')

    def test_registration_user_post_success(self):
        username = self.data['username']

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, status.FOUND)
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)

        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )
