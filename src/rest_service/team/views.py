from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets

# Create your views here.

from .models import Team
from .serializers import TeamSerializers

# Create your views here.

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.annotate(
        total_score=Avg('result__score')
    ).all()

    serializer_class = TeamSerializers