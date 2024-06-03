from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ResultViewSet

router = DefaultRouter()
router.register(
    prefix="results",
    viewset=ResultViewSet,
)

urlpatterns = router.urls