from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """The ModelSerializer for User model"""

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
