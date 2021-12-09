from contents_interview_simulator.api.serializers.general_serializers import InterviewSimulatorModuleStatisticsSerializer

from modules.api.views.modules_viewsets import ModuleViewSet



class InterviewSimulatorModuleStatisticsViewSet(ModuleViewSet):
    serializer_class = InterviewSimulatorModuleStatisticsSerializer

    model_to_format = InterviewSimulatorModuleStatisticsSerializer.Meta.model