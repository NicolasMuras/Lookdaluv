from rest_framework import serializers

from cards.models import Card



class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'completed': instance.completed,
            'rarity': instance.get_rarity_display(),
            'card_module': instance.card_module.__str__(),
        }