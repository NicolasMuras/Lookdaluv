from rest_framework import serializers

from modules.models import Module



class ModuleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Module
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
 
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'level': instance.level,
            'module_type': instance.get_module_type_display(),
        }