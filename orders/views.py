from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from general.views import TitleMixin


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order_create.html'
    form_class = OrderForm
    title = 'Store - Оформление заказа'
