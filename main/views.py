from django.shortcuts import render, redirect
from .models import Genre, Artist, Track
from .forms import GenreForm, ArtistForm, TrackForm

def index(request):
    return render(request, 'index.html')

def genres(request):
    genres_list = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres_list})

def artists(request):
    artists_list = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists_list})

def tracks(request):
    artists_list = Artist.objects.all()
    tracks_list = Track.objects.all()
    current_artist = None

    if request.method == 'POST':
        artist_id = request.POST.get('artist')
        if artist_id:
            current_artist = Artist.objects.get(id=artist_id)
            tracks_list = Track.objects.filter(artist=current_artist)

    return render(request, 'tracks.html', {
        'tracks': tracks_list,
        'artists': artists_list,
        'current_artist': current_artist,
    })

def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genres')
    else:
        form = GenreForm()

    return render(request, 'create_genre.html', {'form': form})

def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')
    else:
        form = ArtistForm()

    return render(request, 'create_artist.html', {'form': form})

def create_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tracks')
    else:
        form = TrackForm()

    return render(request, 'create_track.html', {'form': form})