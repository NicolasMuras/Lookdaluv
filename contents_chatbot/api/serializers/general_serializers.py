from rest_framework import serializers

from contents_chatbot.models import ChatbotModuleStatistics



class ChatbotModuleStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatbotModuleStatistics
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
 
    def to_representation(self, instance):
        return {
            'module': instance.module.__str__(),
            'completed': instance.completed,
            'max_step_reached': instance.max_step_reached,
            'value_generated': instance.value_generated,
            'romance_generated': instance.romance_generated,
            'trap_passed': instance.trap_passed,
        }

class ChatbotModuleStatisticsMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatbotModuleStatistics
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
 
    def to_representation(self, instance):
        return {
            'completed': instance.completed,
            'max_step_reached': instance.max_step_reached,
            'value_generated': instance.value_generated,
            'romance_generated': instance.romance_generated,
            'trap_passed': instance.trap_passed,
        }