from django.urls import include, path
from rest_framework import routers

from .views import UserReadOnlyViewSet

router = routers.SimpleRouter()
router.register(r"", UserReadOnlyViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
