from contents_chatbot.api.serializers.contents_chatbot_serializers import ChatbotModuleSerializer

from modules.api.views.general_views import GeneralViewSet



class ChatbotModuleViewSet(GeneralViewSet):
    serializer_class = ChatbotModuleSerializer

    model_to_format = ChatbotModuleSerializer.Meta.model
