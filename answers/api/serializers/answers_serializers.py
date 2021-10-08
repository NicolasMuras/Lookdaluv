from rest_framework import serializers

from answers.models import Answer
from replys.api.serializers.replys_serializers import ReplyMinimalSerializer



class AnswerSerializer(serializers.ModelSerializer):

    replys = ReplyMinimalSerializer(many=True)
    chatbot_module = serializers.SerializerMethodField()
    answer_category = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['id', 'chatbot_module', 'message', 'answer_category', 'replys']

    def get_chatbot_module(self, instance):
        return instance.chatbot_module.__str__()

    def get_answer_category(self, instance):
        return instance.get_answer_category_display()
