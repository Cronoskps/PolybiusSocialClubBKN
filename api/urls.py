from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='inicio_app'),
    path('games/', views.get_games, name='getgames_app'),
    path('create_game/', views.create_game),
    path('games/<int:id>/', views.detail_game),
    path('delete_game/<int:id>/', views.delete_game),
    path('update_game/<int:id>/', views.update_game),
]