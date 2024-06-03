from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from .models import Result
from .serializers import (
    ResultsSerializer
)

class ResultViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    serializer_class = ResultsSerializer
    queryset = Result.objects.select_related("team").all()
