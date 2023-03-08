from django.db.models import QuerySet

from .models import Link


class LinkRepository:
    @staticmethod
    def get_links() -> QuerySet:
        """Returns all links"""
        return Link.objects.all()

    @staticmethod
    def get_five_recent_links() -> QuerySet:
        """Returns 5 last added links"""
        return LinkRepository.get_links().order_by("-time_created")[:5]
