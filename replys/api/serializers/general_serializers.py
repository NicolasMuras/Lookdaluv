from rest_framework import serializers

from replys.models import Vote



class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'vote_character': instance.get_vote_character_display(),
            'reply': instance.reply.__str__(),
        }