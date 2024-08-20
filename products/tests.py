from http import HTTPStatus as status

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTest(TestCase):

    def test_index_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.OK)
        self.assertTemplateUsed(response, 'products/index.html')
        self.assertEqual(response.context_data['title'], 'Store')


class ProductListViewTest(TestCase):
    fixtures = ['categories.json', 'products.json']

    def setUp(self):
        self.products = Product.objects.all()

    def _general_tests(self, response):
        self.assertEqual(response.status_code, status.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.context_data['title'], 'Store - Каталог')

    def test_product_list_view(self):
        path = reverse('products:products')
        response = self.client.get(path)

        self._general_tests(response=response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products[:3])
        )
