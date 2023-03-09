from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


class UserRepository:
    @staticmethod
    def get_users_with_links() -> QuerySet:
        """Returns all registered users with their links"""
        return User.objects.all().prefetch_related("links")
