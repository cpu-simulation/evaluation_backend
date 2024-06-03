from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ResultViewSet, ScenarioViewSet

router = DefaultRouter()
router.register(
    prefix="results",
    viewset=ResultViewSet,
)
router.register(
    prefix="scenarios",
    viewset=ScenarioViewSet,
)

urlpatterns = router.urls