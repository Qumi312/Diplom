from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):


    context = {
        'title': 'Sweet Home - Главная',
        'content': 'Магазин мебели Sweet Home',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Sweet Home - О нас',
        'content': "О нас",
    }
    return render(request, 'main/about.html', context)

