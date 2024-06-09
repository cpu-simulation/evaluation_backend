from rest_framework import serializers
from .models import Result, Scenario

class ResultsSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name")

    class Meta:
        model = Result
        fields = [
            "id",
            "team_name",
            "team",
            "scenario",
            "status",
            "average_time",
            "score"
        ]

class ScenarioSerializer(serializers.ModelSerializer):
    number_of_steps = serializers.IntegerField()
    class Meta:
        model = Scenario
        fields = ["id", "name", "weight","number_of_steps"]
