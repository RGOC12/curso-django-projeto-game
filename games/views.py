from django.shortcuts import render
from django.http import HttpRequest
from utils.games.games import make_games


def home(request):
    return render(request,'games/pages/home.html')

def game(request,id):
    return render(request,'games/pages/game.html')