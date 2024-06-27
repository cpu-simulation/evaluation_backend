from django.contrib import admin
from .models import Result, Scenario, ScenarioSteps
# Register your models here.

admin.site.register(Result)


class InlineScenarioSteps(admin.TabularInline):
    model = ScenarioSteps


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    inlines = InlineScenarioSteps,