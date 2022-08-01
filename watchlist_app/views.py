from importlib.resources import path
from multiprocessing import context
from urllib import response
from django.shortcuts import render

from watchlist_app import serializers
from .models import Movie
from rest_framework.response import Response
from watchlist_app.serializers import MovieSerializer

# Create your views here.
def movie_list(request):
     if request.method == 'GET':
        movies=Movie.objects.all().order_by('id')
        serializer=MovieSerializer(movies, many=True)
        context={'movies':movies,}
        return render(request, 'movies/movie_list.html', context)
    
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)