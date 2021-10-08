from django.db import models

from simple_history.models import HistoricalRecords

from contents_chatbot.models import ChatbotModule
from core.models import BaseModel


class Answer(BaseModel):

    class AnswerCategory(models.IntegerChoices):

        CONVERSATION_INIT   = 1, "Conversation Init"
        VALUE               = 2, "Generate Value"
        CUALIFICATION       = 3, "Make Her Qualify"
        RATE_HER            = 4, "Rate Her"
        HOT                 = 5, "Hot"
        BORING              = 6, "Boring"
        SIMPL               = 7, "SIMPL"
        ROMANCE             = 8, "Romance"
        BUY                 = 9, "Buy"
        DATE                = 10, "Date"
        TRAP                = 11, "Trap"
        
    message = models.CharField('Message', max_length=100, blank = False, null = False)
    answer_category = models.PositiveSmallIntegerField(
        'Answer Category', 
        choices=AnswerCategory.choices,
        default=AnswerCategory.CONVERSATION_INIT
    )

    chatbot_module = models.ForeignKey(ChatbotModule, on_delete=models.CASCADE, verbose_name='Chatbot Module')

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