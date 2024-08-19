from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import LoginForm, RegistrationForm, ProfileForm
from products.models import Basket
from users.models import User, EmailVerification
from general.views import TitleMixin


class LoginUserView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    title = 'Store - Авторизация'


class RegistrationUserView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно!'
    title = 'Store - Регистрация'


class ProfileUserView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Store - Подтверждение электронной почты'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        user = User.objects.get(email=kwargs.get('email'))
        email_verification = EmailVerification.objects.filter(user=user, code=code)

        if email_verification.exists():
            user.is_verify = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('products:index'))
