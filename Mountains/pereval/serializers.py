from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'otc', 'fam', 'email', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn']


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.ImageField()

    class Meta:
        model = Images
        fields = ['data', 'title']


class MountainSerializer(serializers.ModelSerializer):
    user = UserSerializer
    coords = CoordsSerializer
    level = LevelSerializer
    images = ImagesSerializer

    class Meta:
        model = Mountain
        fields = ['beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images']
