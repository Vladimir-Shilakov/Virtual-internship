from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import User, Coords, Mountain, Level
from .serializers import MountainSerializer


class MountainTestCase(APITestCase):
    def setUp(self):
        user1 = User.objects.create(name='test_name', otc='test_otc', fam='test_fam',
                                    email='test@test.ru', phone='test_phone')
        coords1 = Coords.objects.create(latitude=1.1, longitude=1.1, height=123)
        level1 = Level.objects.create(winter='1a', summer='1b')
        self.mountain1 = Mountain.objects.create(user=user1, coords=coords1, beautyTitle='bt_title',
                                                 title='title', other_titles='other_title', level=level1)

        user2 = User.objects.create(name='test_name2', otc='test_otc2', fam='test_fam2',
                                    email='test2@test.ru', phone='test_phone2')
        coords2 = Coords.objects.create(latitude=1.2, longitude=1.2, height=321)
        level2 = Level.objects.create(autumn='2a', spring='2b')
        self.mountain2 = Mountain.objects.create(user=user2, coords=coords2, beautyTitle='bt_title2',
                                                 title='title', other_titles='other_title', level=level2)

    def test_list_mountain(self):
        response = self.client.get(reverse('mountain-list'))
        serializer_data = MountainSerializer([self.mountain1, self.mountain2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print(serializer_data)

    def test_detail_mountain(self):
        response = self.client.get(reverse('mountain-detail', kwargs={'pk': self.mountain1.id}))
        serializer_data = MountainSerializer(self.mountain1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print(serializer_data)



