from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from .models import Team
from .serializers import TeamSerializers

# Create your views here.

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers