from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


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


class MountainSerializer(WritableNestedModelSerializer):
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
            user = User.objects.create(**user)

        coords = Coords.ojbects.create(**coords)
        level = Level.objects.create(**level)
        images = Images.objects.create(**images)

        mountain = Mountain.ojbects.create(user, coords, level, images, status='new', **validated_data)
        mountain.save()
        return mountain

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            user_fields_for_validation = [
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.fam != data_user['fam'],
                instance_user.email != data_user['email'],
                instance_user.phone != data_user['phone'],
            ]
            if data_user is not None and any(user_fields_for_validation):
                raise serializers.ValidationError(
                    {
                        'message': 'Данные пользователя нельзя изменить',
                    }
                )
        return data

