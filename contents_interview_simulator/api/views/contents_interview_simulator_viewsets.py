from contents_interview_simulator.api.serializers.contents_interview_simulator_serializers import InterviewSimulatorModuleSerializer

from modules.api.views.general_views import GeneralViewSet



class InterviewSimulatorModuleViewSet(GeneralViewSet):
    serializer_class = InterviewSimulatorModuleSerializer

    model_to_format = InterviewSimulatorModuleSerializer.Meta.model
