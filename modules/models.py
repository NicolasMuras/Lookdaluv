from django.db import models

from simple_history.models import HistoricalRecords

from core.models import BaseModel
from users.models import User


class Module(BaseModel):

    class ModuleTypes(models.IntegerChoices):
        QUESTION                    = 1, "Question"
        WORKFLOW                    = 2, "Workflow"
        DECONSTRUCTOR               = 3, "Deconstructor"
        IMAGE_COMPARISION           = 4, "Image Comparision"

    module_type = models.PositiveSmallIntegerField(
        'Module Type', 
        choices=ModuleTypes.choices,
        default=ModuleTypes.QUESTION
    )

    title = models.CharField('Title', max_length=100, blank = False, null = False)
    level = models.IntegerField(default=0, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='module')

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
