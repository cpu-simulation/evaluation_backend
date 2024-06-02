from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

# Create your views here.

from .models import Scenario
from .serializers import ScenarioSerializers

# Create your views here.

class ScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializers