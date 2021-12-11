from rest_framework import serializers

from module_question.models import QuestionModule
from module_question.api.serializers.general_serializers import QuestionModuleStatisticsMinimalSerializer



class QuestionModuleSerializer(serializers.ModelSerializer):

    statistics = QuestionModuleStatisticsMinimalSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()
    difficult = serializers.SerializerMethodField()

    class Meta:
        model = QuestionModule
        fields = ['id', 'title', 'difficult', 'level_steps', 'statistics']
 
    def get_title(self, instance):
        return instance.__str__()

    def get_difficult(self, instance):
        return instance.get_difficult_display()

