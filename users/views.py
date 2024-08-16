from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from users.forms import LoginForm, RegistrationForm, ProfileForm


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


def registration_user(request):

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegistrationForm()
    context = {
        'title': 'Store - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context=context)


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
        'form': form
    }
    return render(request, 'users/profile.html', context=context)
