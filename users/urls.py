from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import LoginUserView, RegistrationUserView, ProfileUserView, logout_user


app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('logout/', logout_user, name='logout'),
]
