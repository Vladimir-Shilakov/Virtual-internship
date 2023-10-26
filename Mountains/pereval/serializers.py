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
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Mountain
        fields = ['beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images']

    def create(self, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        current_user = User.objects.filter(email=user['email'])
        if current_user.exists():
            user_serializer = UserSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = User.objects.create(**user, **validated_data)

        coords = Coords.ojbects.create(**coords, **validated_data)
        level = Level.objects.create(**level, **validated_data)
        images = Images.objects.create(**images, **validated_data)

        mountain = Mountain.ojbects.create(user, coords, level, images, status='new', **validated_data)
        mountain.save()
        return mountain
