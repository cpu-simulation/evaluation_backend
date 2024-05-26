from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Scenario(models.Model): # need more
    id = models.UUIDField(
        _("Id"),
        primary_key=True,
        db_column="scenario_id",
        db_index=True,
        auto_created=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    name = models.CharField(_("Scenario name"), max_length=50)

    weigtht = models.IntegerField() ## it need to be check

    class Meta:
        verbose_name = _("Scenario")
        verbose_name_plural = _("Scenarios")
        db_table = "scenarios"
        

    def __str__(self):
        return self.name

class ScenarioSteps(models.Model): # need more
    scenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    name = models.CharField() # step name
    type = models.CharField() # step type
    input = ...
    output = ...




    class Meta:
        verbose_name = _("Scenario Step") ## need _ ?
        verbose_name_plural = _("Scenario Steps") ## need _ ?
        db_table = "scenario_steps"
        

    def __str__(self):
        return self.name