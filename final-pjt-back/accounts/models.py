from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    point = models.IntegerField(default=100)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers',blank=True)
    
