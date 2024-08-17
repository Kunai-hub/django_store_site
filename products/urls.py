from django.urls import path

from products.views import index, products, basket_add


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
]
