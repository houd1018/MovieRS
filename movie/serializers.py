
from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['image_link', 'name']
