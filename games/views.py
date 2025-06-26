from django.shortcuts import render
from django.http import HttpRequest
from utils.games.games import make_games


def home(request):
    return render(request,'games/pages/home.html', context={
        'games': [make_games() for _ in range(10)]
    })

def game(request,id):
    return render(request,'games/pages/game.html', context={
        'game': make_games(),
        'is_detail_page' : True
    })