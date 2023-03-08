from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from .repository import LinkRepository
from .serializers import LinkSerializer
from .permissions import IsOwnerOrReadOnly


class LinkViewSet(ModelViewSet):
    """The ViewSet that provides all basic actions for Link objects"""
    queryset = LinkRepository.get_links()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    @action(methods=("get",), detail=False)
    def recent(self, request):
        """View-action that returns response with the 5 last added links"""
        recent_links = LinkRepository.get_five_recent_links()

        page = self.paginate_queryset(recent_links)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_links, many=True)
        return Response(serializer.data)
