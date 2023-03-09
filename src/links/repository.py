from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from .models import Link

User = get_user_model()


class LinkRepository:
    @staticmethod
    def get_links() -> QuerySet:
        """Returns all links"""
        return Link.objects.all()

    @staticmethod
    def get_links_of_user(user: User) -> QuerySet:
        """Returns links added by user"""
        return Link.objects.filter(added_by=user)
