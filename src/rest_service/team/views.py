from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Team
from .serializers import TeamSerializers, TeamTestSerializer

# Create your views here.

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.annotate(
        total_score=Avg('result__score')
    ).all()

    serializer_class = TeamSerializers

    def get_serializer_class(self):
        if self.action == "test":
            return TeamTestSerializer
        return super().get_serializer_class()


    @action(detail=True, methods=['post'])
    def test(self, request, pk=None):
        team = get_object_or_404(Team, pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save_task()
        return Response(serializer.data, status=status.HTTP_200_OK)