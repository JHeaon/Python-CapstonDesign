from django.urls import path, include
from . import views
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('BraiileImg', BraiileVeiwSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
