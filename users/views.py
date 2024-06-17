from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Решистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Личный кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...