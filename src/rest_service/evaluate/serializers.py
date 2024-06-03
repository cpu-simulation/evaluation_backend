from rest_framework import serializers
from .models import Result, Scenario

class ResultsSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name")
    class Meta:
        model = Result
        fields = (
            "id",
            "team_name",
            "scenario",
            "status",
            "average_time",
            "score"
        )