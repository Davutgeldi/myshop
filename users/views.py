from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    form = UserLoginForm()
    context = {'title': 'Логин', 'form': form} 
    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {'title': 'Регистрация'} 
    return render(request, 'users/registration.html')


def edit(request):
    context = {'title': 'Редактирование пользователя'}
    return render(request, 'users/edit.html')