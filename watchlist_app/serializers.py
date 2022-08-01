from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name  = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=250)
    is_active = serializers.BooleanField(default=True)