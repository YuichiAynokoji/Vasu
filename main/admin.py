from django.contrib import admin
from .models import Genre, Artist, Track

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en')
    search_fields = ('name_ru', 'name_en')
    ordering = ('id',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'artist')
    search_fields = ('title',)
    list_filter = ('genres', 'artist')
    ordering = ('id',)
    filter_horizontal = ('genres',)