from rest_framework import viewsets

from .repository import UserRepository
from .serializers import UserSerializer


class UserReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """The ViewSet that provides read-only actions for User objects"""
    queryset = UserRepository.get_users()
    serializer_class = UserSerializer
