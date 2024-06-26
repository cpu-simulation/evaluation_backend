from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]