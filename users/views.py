from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.forms import LoginForm, RegistrationForm, ProfileForm
from products.models import Basket
from users.models import User


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data(**kwargs)
        context['title'] = 'Store - Авторизация'
        return context


class RegistrationUserView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(RegistrationUserView, self).get_context_data(**kwargs)
        context['title'] = 'Store - Регистрация'
        return context


class ProfileUserView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['title'] = 'Store - Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:index'))
