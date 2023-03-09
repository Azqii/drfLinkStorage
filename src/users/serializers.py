from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework import serializers

from links.serializers import LinkSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """The ModelSerializer for the User model"""

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class FullUserSerializer(serializers.ModelSerializer):
    """
    The ModelSerializer for the User model with all fields.
    Made for admins.
    """
    links = LinkSerializer(many=True, read_only=True)
    days_registered = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ("groups", "user_permissions")

    def get_days_registered(self, obj):
        return (now() - obj.date_joined).days
