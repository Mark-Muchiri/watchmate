from rest_framework import serializers
from watchlist_app .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name  = serializers.CharField(max_length=50)
    movie_description = serializers.CharField(max_length=250)
    is_active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.movie_description = validated_data.get('movie_description', instance.movie_description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance