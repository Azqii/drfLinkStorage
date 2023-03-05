from rest_framework import routers
from django.urls import path, include

from .views import LinkViewSet

router = routers.SimpleRouter()
router.register(r"", LinkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
