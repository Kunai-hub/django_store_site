from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from users.forms import LoginForm, RegistrationForm, ProfileForm
from products.models import Basket
from users.models import User


def login_user(request):

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = LoginForm()
    context = {
        'title': 'Store - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


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
