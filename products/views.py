from django.shortcuts import render

from products.models import Product, ProductCategory


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
