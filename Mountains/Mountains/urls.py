from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from pereval import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'coords', views.CoordViewSet)
router.register(r'levels', views.LevelViewSet)
router.register(r'images', views.ImagesViewSet)
router.register(r'mountain', views.MountainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


