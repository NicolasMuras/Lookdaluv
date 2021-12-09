from rest_framework import serializers

from contents_interview_simulator.models import InterviewSimulatorModule
from contents_interview_simulator.api.serializers.general_serializers import InterviewSimulatorModuleStatisticsMinimalSerializer



class InterviewSimulatorModuleSerializer(serializers.ModelSerializer):

    statistics = InterviewSimulatorModuleStatisticsMinimalSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()
    difficult = serializers.SerializerMethodField()

    class Meta:
        model = InterviewSimulatorModule
        fields = ['id', 'title', 'difficult', 'level_steps', 'statistics']
 
    def get_title(self, instance):
        return instance.__str__()

    def get_difficult(self, instance):
        return instance.get_difficult_display()

