from django.db import models

from simple_history.models import HistoricalRecords

from contents_interview_simulator.models import InterviewSimulatorModule
from core.models import BaseModel


class Answer(BaseModel):

    class AnswerCategory(models.IntegerChoices):

        CONVERSATION_INIT   = 1, "Conversation Init"
        VALUE               = 2, "Generate Value"
        CUALIFICATION       = 3, "Make Her Qualify"
        RATE_HER            = 4, "Rate Her"
        HOT                 = 5, "Hot"
        BORING              = 6, "Boring"
        BUY                 = 9, "Buy"

        
    message = models.CharField('Message', max_length=100, blank = False, null = False)
    answer_category = models.PositiveSmallIntegerField(
        'Answer Category', 
        choices=AnswerCategory.choices,
        default=AnswerCategory.CONVERSATION_INIT
    )

    interview_simulator_module = models.ForeignKey(InterviewSimulatorModule, on_delete=models.CASCADE, verbose_name='Interview Simulator Module')

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):

        return self.message