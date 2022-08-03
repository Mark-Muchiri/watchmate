from importlib.resources import path
from multiprocessing import context
from urllib import request, response
from django.shortcuts import render

from watchlist_app import serializers
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.serializers import MovieSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies=Movie.objects.all().order_by('id')
        serializer=MovieSerializer(movies, many=True)
        context={'movies':movies,}
        return Response(serializer.data)
        # return render(request, 'movies/movie_list.html', context)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
def movie_detail(request, pk):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def movie_detail(request,pk):
    if request.method == 'GET':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response (serializer.data)
    if request.method =='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)