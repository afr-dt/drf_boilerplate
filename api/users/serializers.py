# Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
