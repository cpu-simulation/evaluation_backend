from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Scenario(models.Model): # need more

    name = models.CharField(_("Scenario name"), max_length=50)

    weight = models.IntegerField() ## it need to be check

    class Meta:
        verbose_name = _("Scenario")
        verbose_name_plural = _("Scenarios")
        db_table = "scenarios"
        

    def __str__(self):
        return self.name

class ScenarioSteps(models.Model): # need more
    scenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    name = models.CharField(max_length=50) # step name
    type = models.CharField(max_length=50) # step type
    input = ...
    output = ...




    class Meta:
        verbose_name = _("Scenario Step") ## need _ ?
        verbose_name_plural = _("Scenario Steps") ## need _ ?
        db_table = "scenario_steps"
        

    def __str__(self):
        return self.name