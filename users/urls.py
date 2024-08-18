from django.urls import path

from users.views import login_user, RegistrationUserView, profile_user, logout_user


app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile/', profile_user, name='profile'),
    path('logout/', logout_user, name='logout'),
]
