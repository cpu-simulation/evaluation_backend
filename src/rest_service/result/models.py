from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Result(models.Model):
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

    # In team_id ForeignKey cant write 'team.Team.id'
    # is 'team.Team' ok?
    # This goes for scenario_id too..
    team_id = models.ForeignKey('team.Team', on_delete=models.CASCADE)  # should on_delete stayed on CASCADE or change?
    scenario_id = models.ForeignKey('test.Scenario', on_delete=models.CASCADE) # should on_delete stayed on CASCADE or change?
    
    avarage_time = models.IntegerField() # i think it need to change !!
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    upadated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")
        db_table = "results"
        

    def __str__(self):
        return self.score ## be this or not?