from django.urls import path

from users.views import login_user, registration_user, profile_user, logout_user


app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration'),
    path('profile/', profile_user, name='profile'),
    path('logout/', logout_user, name='logout'),
]
