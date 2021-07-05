from django.urls import path, include
from rest_framework import routers

from api.users.views import UserAPIView


router = routers.DefaultRouter()
router.register('users', UserAPIView)

urlpatterns = [
    path('', include(router.urls))
]
