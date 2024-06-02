from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Result(models.Model):
    class RESULT_STATUS(models.TextChoices):
        PENDING = "W", _("WAITING")
        FAILED = "F", _("Failed")
        DONE = "P", _("PASSED")

    id = models.UUIDField(
        _("Id"),
        primary_key=True,
        db_column="result_id",
        db_index=True,
        auto_created=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        db_column="team_id",
        )
    scenario = models.ForeignKey(
        'test.Scenario',
        on_delete=models.CASCADE,
        db_column="scenario_id",
        )
    status = models.CharField(
        _("Status"),
        max_length=1,
        choices=RESULT_STATUS.choices,
        default=RESULT_STATUS.PENDING
        )
    average_time = models.IntegerField() # i think it need to change !!
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")
        db_table = "results"
        

    def __str__(self):
        return f"{self.team} - {self.scenario}: {self.score}"