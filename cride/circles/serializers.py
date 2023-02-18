"""Circle serializers"""

# Django REST Framework
from rest_framework import serializers

class CircleSerializer(serializers.Serializer):
    """Circle serializer"""
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()
    

class CreateCircleSerializer(serializers.Serializer):
    """Create circle serializer"""
    name = serializers.CharField(max_length=140)
    slug_name = serializers.Slugfield(max_length=40)
    about = serializers.CharField(
        max_length=255,
        required=False
    )