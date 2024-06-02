from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins 
from .serializers import ResultsSerializer
from .models import Result
# Create your views here.

class ResultViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    serializer_class = ResultsSerializer
    queryset = Result.objects.select_related("team").all()
