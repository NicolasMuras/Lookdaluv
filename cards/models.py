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

        return self.module_type


class Card(BaseModel):

    class CardsRarities(models.IntegerChoices):
        WHITE   = 1, "WHITE"
        GREEN   = 2, "GREEN"
        BLUE    = 3, "BLUE"
        PURPLE  = 4, "PURPLE"
        ORANGE  = 5, "ORANGE"
        RED     = 6, "RED"


    title = models.CharField('Title', max_length=100, blank = False, null = False)
    description = models.TextField('Description', max_length=500, blank = False, null = False)
    completed = models.BooleanField(blank=False, null=False, default=False)
    rarity = models.PositiveSmallIntegerField(
        'Rarity', 
        choices=CardsRarities.choices,
        default=CardsRarities.WHITE
    )

    card_module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Card Module')

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

        return self.title