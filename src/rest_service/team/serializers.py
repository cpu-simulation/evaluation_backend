from rest_framework import serializers
from .models import Team

class TeamSerializers(serializers.ModelSerializer):
    total_score = serializers.FloatField()

    class Meta:
        model = Team
        fields = ["id", "name", "members", "total_score", "has_website", "used_template"]

class TeamTestSerialzers(serializers.ModelSerializer):
    test_field = serializers.CharField(required=True)

    class Meta:
        model = Team
        fields = ['test_field']
