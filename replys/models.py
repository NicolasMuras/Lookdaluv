from django.db import models

from simple_history.models import HistoricalRecords

from answers.models import Answer
from core.models import BaseModel



class Reply(BaseModel):

    class ReplyCharacter(models.IntegerChoices):
        POSITIVE         = 1, "POSITIVE"
        NEUTRAL          = 2, "NEUTRAL"
        NEGATIVE         = 3, "NEGATIVE"
        TRAP             = 4, "TRAP"

    reply_character = models.PositiveSmallIntegerField(
        'Reply Character', 
        choices=ReplyCharacter.choices,
        default=ReplyCharacter.NEUTRAL
    )

    message = models.CharField('Reply Message', max_length=100, blank = False, null = False)

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Answer', related_name='replys')

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Reply'
        verbose_name_plural = 'Replys'

    def __str__(self):

        return self.message


class Vote(BaseModel):

    class VoteCharacter(models.IntegerChoices):
        POSITIVE         = 1, "POSITIVE"
        NEUTRAL          = 2, "NEUTRAL"
        NEGATIVE         = 3, "NEGATIVE"
        TRAP             = 4, "TRAP"

    vote_character = models.PositiveSmallIntegerField(
        'Vote Character', 
        choices=VoteCharacter.choices,
        default=VoteCharacter.NEUTRAL
    )

    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, verbose_name='Reply', related_name='vote')

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
