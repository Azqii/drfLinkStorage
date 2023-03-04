from django.db.models import QuerySet

from .models import Link


class LinkRepository:
    @staticmethod
    def get_links() -> QuerySet:
        """Returns all links"""
        return Link.objects.all()
