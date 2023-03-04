from rest_framework import viewsets, permissions

from .repository import LinkRepository
from .serializers import LinkSerializer
from .permissions import IsOwnerOrReadOnly


class LinkViewSet(viewsets.ModelViewSet):
    """The ViewSet that provides all basic actions for Link objects"""
    queryset = LinkRepository.get_links()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
