from django.db import models

from simple_history.models import HistoricalRecords

from core.models import BaseModel
from modules.models import Module



class QuestionModule(Module):

    class Difficult(models.IntegerChoices):

        VERY_EASY               = 1, "Very Easy"
        EASY                    = 2, "Easy"
        MEDIUM                  = 3, "Medium"
        HARD                    = 4, "Hard"
        VERY_HARD               = 5, "Very Hard"
        NIGHTMARE               = 6, "Nightmare"

    difficult = models.PositiveSmallIntegerField(
        'Difficult', 
        choices=Difficult.choices,
        default=Difficult.MEDIUM
    )
    
    level_steps = models.IntegerField(default=10)
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Question Module'
        verbose_name_plural = 'Question Modules'

    def __str__(self):

        return self.title


class QuestionModuleStatistics(BaseModel):

    module = models.ForeignKey(QuestionModule, on_delete=models.CASCADE, verbose_name='Module', related_name='statistics')

    completed = models.BooleanField(blank=False, null=False, default=False)
    max_step_reached = models.IntegerField(default=1)
    value_generated = models.IntegerField(default=1)
    trap_passed = models.BooleanField(blank=True, null=False, default=False)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Question Statistic'
        verbose_name_plural = 'Question Statistics'

    def __str__(self):

        return self.module.title