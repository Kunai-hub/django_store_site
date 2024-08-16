from django.urls import path

from users.views import login_user, registration_user


app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration'),
]
