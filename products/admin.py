from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'image', ('price', 'quantity'), 'category')
    search_fields = ('name',)
    readonly_fields = ('description',)
    ordering = ('name',)


class BasketAdmin(admin.StackedInline):
    model = Basket

    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
