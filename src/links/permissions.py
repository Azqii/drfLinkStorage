from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission that allows only owners to edit/delete their objects.
    Read-only for everyone else.
    """
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and obj.added_by == request.user
        )
