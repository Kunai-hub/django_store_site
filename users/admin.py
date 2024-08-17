from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    # fields = ('username', 'first_name','last_name', 'email', 'image', ('is_active', 'is_staff', 'is_superuser'),
    #           'date_joined', 'last_login')
    search_fields = ('username',)
    ordering = ('id',)
    inlines = (BasketAdmin,)

