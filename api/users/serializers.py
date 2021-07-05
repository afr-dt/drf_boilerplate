# Rest Framework
from rest_framework import serializers

# Models
from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
