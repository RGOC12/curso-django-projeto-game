from django.shortcuts import render
from django.http import HttpRequest
from .models import game


games = game.objects.all().order_by('-id')

def home(request):
    return render(request,'games/pages/home.html', context={
        'games': games
    })

def game(request,id):
    return render(request,'games/pages/game.html', context={
        'game': make_games(),
        'is_detail_page' : True
    })