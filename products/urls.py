from django.urls import path

from products.views import index, products, basket_add, basket_remove


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/category/<int:category_id>/', products, name='products_category'),
    path('products/page/<int:page_number>/', products, name='products_page'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
