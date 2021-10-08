from django.db import models

from simple_history.models import HistoricalRecords

from core.models import BaseModel



class Module(BaseModel):

    class ModuleTypes(models.IntegerChoices):
        PERSONAL_GROWTH         = 1, "Personal Growth"
        CHAT_BOT                = 2, "Chat Bot"
        SIMPL_DECONSTRUCTOR     = 3, "Simpl Deconstructor"
        DATE_SIMULATION         = 4, "Date Simulation"
        SEX_ARTS                = 5, "Sex Secrets"
        ENVIRONMENT_DOMINANCE   = 6, "Environment Dominance"

    module_type = models.PositiveSmallIntegerField(
        'Module Type', 
        choices=ModuleTypes.choices,
        default=ModuleTypes.PERSONAL_GROWTH
    )

    title = models.CharField('Title', max_length=100, blank = False, null = False)
    level = models.IntegerField(default=0, null=False, blank=False)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):

        return self.title
