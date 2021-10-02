from rest_framework import serializers

from cards.models import Module



class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')