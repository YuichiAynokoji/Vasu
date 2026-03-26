from django.shortcuts import render
from .models import Genre

def index(request):
    return render(request, 'index.html')

def genres(request):
    genres_list = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres_list})