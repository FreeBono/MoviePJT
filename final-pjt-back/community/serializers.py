
from rest_framework import serializers
from accounts.serializers import UserSerializer
# from rest_framework.exceptions import server_error
from .models import Comment, Review
from django.core.serializers import serialize
from accounts.models import User
from movies.models import Movie
#유저네임, 타이틀, ,컨텐츠, 평점, 랭크무비타이틀,
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):

    userreviews = ReviewSerializer(many=True, read_only=True)
    followers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username','userreviews','point','date_joined','followings','followers',)


class CommentListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Review
        fields = ('id','rank','movie','title','content','created_at','updated_at','username', 'movietitle','user','like','comments')




