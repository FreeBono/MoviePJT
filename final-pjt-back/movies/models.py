from django.db import models



# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_id = models.IntegerField()
    adult = models.BooleanField(null=True)
    backdrop_path = models.TextField(null=True)
    genre_ids = models.TextField(null=True)
    original_language = models.CharField(max_length=100,null=True)
    original_title = models.TextField(null=True)
    video = models.BooleanField(null=True)
    vote_count = models.IntegerField(null=True)
    title = models.CharField(max_length=30,null=True)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    release_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.movie_id}'

class UpcomingMovie(models.Model):
    movie_id = models.IntegerField()
    adult = models.BooleanField(null=True)
    backdrop_path = models.TextField(null=True)
    genre_ids = models.TextField(null=True)
    original_language = models.CharField(max_length=100,null=True)
    original_title = models.TextField(null=True)
    video = models.BooleanField(null=True)
    vote_count = models.IntegerField(null=True)
    title = models.CharField(max_length=30,null=True)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    release_date = models.DateField(null=True)
