from http import HTTPStatus as status

from django.test import TestCase
from django.urls import reverse


class RegistrationUserViewTest(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')

    def test_registration_user_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, status.OK)
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
