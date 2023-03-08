from rest_framework.viewsets import ReadOnlyModelViewSet

from .repository import UserRepository
from .serializers import UserSerializer, FullUserSerializer


class UserReadOnlyViewSet(ReadOnlyModelViewSet):
    """The ViewSet that provides read-only actions for User objects"""
    queryset = UserRepository.get_users()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullUserSerializer
        return UserSerializer
