from django.conf import settings

from rest_framework import serializers

from .models import Team
from .task_manager import push_task

class TeamSerializers(serializers.ModelSerializer):
    total_score = serializers.FloatField()

    class Meta:
        model = Team
        fields = ["id", "name", "members", "total_score", "has_website", "used_template"]

class TeamTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = []

    def save_task(self):
        msg = {
            "team_id": f"{self.instance.id}",
            "url": f"api.{self.instance.name}.dev"
        }
        push_task(msg=msg)
