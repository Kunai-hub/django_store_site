from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store'
    }

    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Store - Каталог'
    }

    return render(request, 'products/products.html', context=context)
