from rest_framework import serializers
from .models import Result, Scenario

class ResultsSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name")
    scenario = serializers.HyperlinkedRelatedField(view_name="scenario-detail", read_only=True)
    status = serializers.SerializerMethodField()

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

    def get_status(self, obj):
        return Result.RESULT_STATUS(obj.status).name
    
    
class ScenarioSerializer(serializers.ModelSerializer):
    number_of_steps = serializers.IntegerField()
    class Meta:
        model = Scenario
        fields = ["id", "name", "weight", "number_of_steps"]
