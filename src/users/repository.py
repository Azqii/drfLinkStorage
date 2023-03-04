from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


class UserRepository:
    @staticmethod
    def get_users() -> QuerySet:
        """Returns all registered users"""
        return User.objects.all()
