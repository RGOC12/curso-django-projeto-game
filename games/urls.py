from django.urls import path
from games import views
urlpatterns = [
    path('', views.home),
    path('game/<int:id>', views.game),
]
