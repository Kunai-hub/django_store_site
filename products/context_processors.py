from products.models import Basket


def baskets(request):
    user = request.user
    user_basket = Basket.objects.filter(user=user.id)
    return {'baskets': user_basket if user.is_authenticated else []}
