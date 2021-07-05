# REST Framework
from rest_framework import status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Django models
from api.users.models import User

# Serializers
from api.users.serializers import UserSerializer


class UserAPIView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
