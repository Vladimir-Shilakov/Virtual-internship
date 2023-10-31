import django_filters
from rest_framework.response import Response

from .serializers import *
from rest_framework import viewsets, status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class MountainViewSet(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user__email"]

    def create(self, request, *args, **kwargs):
        serializer = MountainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Отправлено успешно',
                    'id': serializer.data[id]
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': serializer.errors
                }
            )
        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'BAD REQUEST'
                }
            )

    def partial_update(self, request, *args, **kwargs):
        mount_update = self.get_object()
        if mount_update.status == 'new':
            serializer = MountainSerializer(mount_update, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': 1,
                        'message': 'Изменения сохраненны'
                    }
                )
            else:
                return Response(
                    {
                        'state': 0,
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': 0,
                    'message': f'Пост находится в статусе:{mount_update.get_status_display()}, Изменения невозможны'
                }
            )
