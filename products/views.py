from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import Product, ProductCategory, Basket


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Store - Каталог',
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if baskets.exists():
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
