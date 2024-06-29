from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.

from .models import Team
from .serializers import TeamSerializers, TeamTestSerialzers

# Create your views here.

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.annotate(
        total_score=Avg('result__score')
    ).all()

    serializer_class = TeamSerializers

    @action(detail=True, methods=['post'])
    def test(self, request, pk=None):
        team = get_object_or_404(Team, pk=pk)
        serializer = TeamTestSerialzers

        if serializer.is_valid():
            ...
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    