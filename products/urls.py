from django.urls import path

from products.views import (IndexView, ProductListView, basket_add,
                            basket_remove)

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/category/<int:category_id>/', ProductListView.as_view(), name='products_category'),
    path('products/page/<int:page>/', ProductListView.as_view(), name='products_page'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
