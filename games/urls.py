from django.urls import path
from games import views
urlpatterns = [
    path('', views.home, name = "games-home"),
    path('game/<int:id>', views.game, name = "games-game"),
]
