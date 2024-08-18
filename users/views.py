from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

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


@login_required
def profile_user(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context=context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:index'))
