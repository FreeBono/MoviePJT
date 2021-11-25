from rest_framework import serializers
from .models import Genre,Movie, UpcomingMovie


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('pk','name')

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class UpcomingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpcomingMovie
        fields = '__all__'

