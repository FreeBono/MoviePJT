from random import random
from django.contrib.auth import SESSION_KEY, get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import random
from .serializers import UserSerializer
from community.serializers import UserListSerializer
from .models import User
from django.shortcuts import get_object_or_404


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user= serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def userlist(request):
    if request.method == 'GET':
        users = User.objects.order_by('-point')[:3]
        users_default = [{'username': 'defaultuser1', 'point': 100},
        {'username': 'defaultuser2', 'point': 120},
        {'username': 'defaultuser3', 'point': 90}]
        serializer = UserSerializer(users, many = True)
        users_default += serializer.data 
        users_default.sort(key= lambda x:x['point'],reverse=True)
        return Response(users_default[:3])


@api_view(['POST'])
def userpoint(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        if request.data['where'] == 'wr':
            user.point = user.point + 100
            user.save()
        elif request.data['where'] == 'rr':
            user.point = user.point - 20
            user.save()
        elif request.data['where'] == 'wc':
            user.point = user.point + 10
            user.save()
        elif request.data['where'] == 'pmr':
            user.point = user.point - random.sample(range(100,200,10),1)[0]
            user.save()
        elif request.data['where'] == 'logo':
            user.point = user.point + 1
            user.save()
        else:
            user2 = User.objects.get(username=request.data['where'])
            if request.data['where'] == str(user2):
                user2.point = user2.point + 10
                user2.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def profile(request,username):
    user = User.objects.filter(username=username)    
    serializer = UserListSerializer(user,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request):
    you = get_object_or_404(get_user_model(), username = request.data.get('profileName'))
    me = request.user
    if you != me :
        # print(you.followers.filter(pk=me.pk))  
        if you.followers.filter(pk=request.user.pk).exists(): 
            you.followers.remove(me)
            following = False
        else : 
            you.followers.add(me)
            following = True
        context = {
            'following' : following,
            'follower_count' : you.followers.count(),
            'following_count' : you.followings.count()
        }
        return Response(context,status=status.HTTP_201_CREATED)
