from django.urls import include, path
from rest_framework import routers

from .views import UserReadOnlyViewSet

router = routers.SimpleRouter()
router.register(r"users", UserReadOnlyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
