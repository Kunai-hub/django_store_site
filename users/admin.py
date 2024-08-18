from django.contrib import admin

from users.models import User, EmailVerification
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    # fields = ('username', 'first_name','last_name', 'email', 'image', ('is_active', 'is_staff', 'is_superuser'),
    #           'date_joined', 'last_login')
    search_fields = ('username',)
    ordering = ('id',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expiration',)
    fields = ('user', 'code', 'created_timestamp', 'expiration',)
    readonly_fields = ('created_timestamp',)
