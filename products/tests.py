from http import HTTPStatus as status

from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_index_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.OK)
        self.assertTemplateUsed(response, 'products/index.html')
        self.assertEqual(response.context_data['title'], 'Store')
