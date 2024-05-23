from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Team(models.Model):

    id = models.IntegerField(
        _("Id"),
        primary_key=True,
        db_column="team_id",
        db_index=True,
        auto_created=True
    )
    name = models.CharField(
        _("Team name"),
        max_length=50,
        )
    #TODO: Add more fields

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        db_table = "teams"
        

    def __str__(self):
        return self.name
