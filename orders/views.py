from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderForm
from general.views import TitleMixin


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order_create.html'
    form_class = OrderForm
    title = 'Store - Оформление заказа'
    success_url = reverse_lazy('orders:create')

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        return super(OrderCreateView, self).form_valid(form)
