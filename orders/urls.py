from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('canceled/', CanceledTemplateView.as_view(), name='canceled'),
    path('', OrderListView.as_view(), name='order_list'),
    path('<int:pk>', OrderDetailView.as_view(), name='order_list_detail'),
]
