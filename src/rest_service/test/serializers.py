from rest_framework import serializers
from .models import Scenario, ScenarioSteps

class ScenarioSerializers(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        fields = ["name", "weight"]

