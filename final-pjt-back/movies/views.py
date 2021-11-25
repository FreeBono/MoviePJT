from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from .models import Movie, UpcomingMovie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import datetime
import random

@api_view(['GET'])

def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many= True)
    
        return Response(serializer.data)
     
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_latest(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(release_date__lte=datetime.datetime.now().date()).order_by('-release_date')[:20]

        serializer = MovieSerializer(movies, many= True)
        return Response(serializer.data)
     
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_upcoming(request):
    if request.method == 'GET':
        movies = UpcomingMovie.objects.all()

        serializer = MovieSerializer(movies, many= True)
        randomdata = random.sample(serializer.data,4)


        return Response(randomdata)




@api_view(['GET'])
@permission_classes([AllowAny])
def movie_popular(request):
    if request.method == 'GET':
        movies = Movie.objects.all()[:10]
        serializer = MovieSerializer(movies, many= True)
    
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_top_rated(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(vote_count__gte=1000).order_by('-vote_average')[:10]
        serializer = MovieSerializer(movies, many= True)
    
        return Response(serializer.data)

@api_view(['GET'])
def givemovieid(request,movie_id):
   
    if request.method =='GET':
        movie = Movie.objects.filter(id=movie_id)
        serializer = MovieSerializer(movie,many=True)

        return Response(serializer.data)


@api_view(['GET'])
def casemovie(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-vote_count')[:100]
        serializer = MovieSerializer(movies, many= True)
        randomdata = random.sample(serializer.data,12)
        return Response(randomdata)



