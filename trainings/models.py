from django.db import models

class TrainingModule(models.Model):

    name = models.CharField('Nombre', max_length=100, blank=True, null=True)
    description = models.CharField('Descripción', max_length=500, blank=True, null=True)