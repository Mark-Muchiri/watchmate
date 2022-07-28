from importlib.resources import path
from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_list(request):
    movies=Movie.objects.all().order_by('id')
    return render(request, 'movies/movie_list.html')