from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, LoginUserView, ProfileUserView,
                         RegistrationUserView)

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='email_verification'),
]
