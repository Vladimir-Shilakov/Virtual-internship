from django.urls import path, include
from .views import MountainViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mountain', MountainViewSet, basename='mountain')

urlpatterns = [
    path('submitData/', include(router.urls)),
]
