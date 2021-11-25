from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer
from community.serializers import ReviewSerializer,CommentSerializer,CommentListSerializer
from django.db.models import F, Sum, Count, Case, When
from .models import Review,Movie,Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.contrib.auth.decorators import login_required
from accounts.models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# Create your views here.


@api_view(['POST','GET'])

def review(request):
    if request.method =='GET':
        reviews = Review.objects.order_by('-pk')
        serializer = CommentListSerializer(reviews,many=True)
        
        return Response(serializer.data)

    if request.method == 'POST':
        # print(request.user)
        movie = Movie.objects.filter(movie_id=request.data.get('movie_id')).first()
        username = request.user
        serializer = ReviewSerializer(data=request.data)
    
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie, username=username,)
          
            return Response(serializer.data)



@api_view(['DELETE','GET','PUT'])
def reviewrevise(request,review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method =='GET':
        serializer = ReviewSerializer(review)
        
        return Response(serializer.data)
    
    if request.method =='DELETE':
        if request.user == review.user:
            review.delete()
            return Response({'name': review_id}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST','GET'])
def comment(request,review_id):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True,):
            serializer.save(username=request.user,review_id=review_id)
          
            return Response(serializer.data)
    elif request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_id)
        # print(comments)
        
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
        # return Response(serializer.data)





@api_view(['DELETE','PUT'])
def commentrevise(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method =='DELETE':
        # if request.user == comment.username:
        comment.delete()
        return Response({'id': comment_id}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = CommentSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([AllowAny])
def like(request):
    review_pk = request.data.get('reviewId')
    user = request.user
    review = get_object_or_404(Review,pk=review_pk)
    
    if review.like.filter(pk=user.pk).exists():
        review.like.remove(user)
        liked = False
    else:
        review.like.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': review.like.count()
    }
    return Response(context, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def reviewking(request):
    if request.method=="GET":
        reviews = Review.objects.annotate(num_like=Count('like')).order_by('-num_like')[:10]
        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

# 테스트용 주석