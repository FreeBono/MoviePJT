from django.db import models
from movies.models import Movie
from accounts.models import User
from django.conf import settings
# Create your models here.


class Review(models.Model):

    rank = models.IntegerField(null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews',null=True)
    title = models.CharField(max_length=500,blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    username = models.TextField(null=True)
    movietitle = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='userreviews',null=True,)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review', blank= True, )
    def __str__(self):  
        return f'{self.pk} : {self.like}'


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,related_name='comments',null=True)
    content = models.TextField()
    username = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




