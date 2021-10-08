from rest_framework import serializers

from replys.models import Reply



class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'message': instance.message,
            'reply_character': instance.get_reply_character_display(),
            'answer': instance.answer.__str__(),
        }

class ReplyMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'message': instance.message,
        }