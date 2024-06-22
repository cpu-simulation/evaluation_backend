from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.


class Team(models.Model):
    id = models.UUIDField(
        _("Id"),
        primary_key=True,
        db_column="team_id",
        db_index=True,
        auto_created=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )
    
    name = models.CharField(
        _("Team name"),
        max_length=50,
        )
    
    members = models.JSONField(default=list)

    has_website = models.BooleanField() # 0 = core | 1 = website

    used_template = models.BooleanField() # 0 = not used temp | 1 = used temp 

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        db_table = "teams"
        

    def __str__(self):
        return self.name
