from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genres/', views.genres, name='genres'),
    path('artists/', views.artists, name='artists'),
    path('tracks/', views.tracks, name='tracks'),

    path('genres/create/', views.create_genre, name='create_genre'),
    path('artists/create/', views.create_artist, name='create_artist'),
    path('tracks/create/', views.create_track, name='create_track'),
]