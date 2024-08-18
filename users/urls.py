from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login_user, RegistrationUserView, ProfileUserView, logout_user


app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('logout/', logout_user, name='logout'),
]
