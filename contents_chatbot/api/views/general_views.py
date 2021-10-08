from contents_chatbot.api.serializers.general_serializers import ChatbotModuleStatisticsSerializer

from modules.api.views.modules_viewsets import ModuleViewSet



class ChatbotModuleStatisticsViewSet(ModuleViewSet):
    serializer_class = ChatbotModuleStatisticsSerializer

    model_to_format = ChatbotModuleStatisticsSerializer.Meta.model