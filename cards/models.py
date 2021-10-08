from django.db import models

from simple_history.models import HistoricalRecords

from core.models import BaseModel
from modules.models import Module



class Card(BaseModel):

    class CardsRarities(models.IntegerChoices):
        WHITE   = 1, "WHITE"
        GREEN   = 2, "GREEN"
        BLUE    = 3, "BLUE"
        PURPLE  = 4, "PURPLE"
        ORANGE  = 5, "ORANGE"
        RED     = 6, "RED"


    description = models.TextField('Description', max_length=500, blank = False, null = False)
    completed = models.BooleanField(blank=False, null=False, default=False)
    rarity = models.PositiveSmallIntegerField(
        'Rarity', 
        choices=CardsRarities.choices,
        default=CardsRarities.WHITE
    )

    card_module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Card Module', related_name='card')

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):

        return self.card_module.title