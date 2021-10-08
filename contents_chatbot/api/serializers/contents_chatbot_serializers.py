from rest_framework import serializers

from contents_chatbot.models import ChatbotModule
from contents_chatbot.api.serializers.general_serializers import ChatbotModuleStatisticsMinimalSerializer



class ChatbotModuleSerializer(serializers.ModelSerializer):

    statistics = ChatbotModuleStatisticsMinimalSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()
    difficult = serializers.SerializerMethodField()

    class Meta:
        model = ChatbotModule
        fields = ['id', 'title', 'difficult', 'level_steps', 'statistics']
 
    def get_title(self, instance):
        return instance.__str__()

    def get_difficult(self, instance):
        return instance.get_difficult_display()

