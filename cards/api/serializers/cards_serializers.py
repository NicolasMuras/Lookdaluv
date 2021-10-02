from rest_framework import serializers

from cards.models import Card
from cards.api.serializers.generals_serializer import ModuleSerializer



class CardListCreateUpdateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Card
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.title,
            'description': instance.description,
            'completed': instance.completed,
            'rarity': instance.rarity,
            'card_module': instance.card_module.module_type,
        }