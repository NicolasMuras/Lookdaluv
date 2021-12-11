from rest_framework import serializers

from module_question.models import QuestionModuleStatistics



class QuestionModuleStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModuleStatistics
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
 
    def to_representation(self, instance):
        return {
            'module': instance.module.__str__(),
            'completed': instance.completed,
            'max_step_reached': instance.max_step_reached,
            'value_generated': instance.value_generated,
            'trap_passed': instance.trap_passed,
        }

class QuestionModuleStatisticsMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModuleStatistics
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
 
    def to_representation(self, instance):
        return {
            'completed': instance.completed,
            'max_step_reached': instance.max_step_reached,
            'value_generated': instance.value_generated,
            'trap_passed': instance.trap_passed,
        }