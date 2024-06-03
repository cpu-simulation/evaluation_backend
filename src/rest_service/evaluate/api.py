from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import (
    GenericViewSet,
    mixins,
    ReadOnlyModelViewSet
)
from .models import Result, Scenario
from .serializers import (
    ResultsSerializer,
    ScenarioSerializer,
)

class ResultViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    serializer_class = ResultsSerializer
    queryset = Result.objects\
        .select_related("team").all()



class ScenarioViewSet(ReadOnlyModelViewSet):
    queryset = Scenario.objects.annotate(number_of_steps=Count("steps")).all()
    serializer_class = ScenarioSerializer
