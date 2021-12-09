from contents_chatbot.api.serializers.contents_chatbot_serializers import InterviewSimulatorModuleSerializer

from modules.api.views.general_views import GeneralViewSet



class InterviewSimulatorModuleViewSet(GeneralViewSet):
    serializer_class = InterviewSimulatorModuleSerializer

    model_to_format = InterviewSimulatorModuleSerializer.Meta.model
