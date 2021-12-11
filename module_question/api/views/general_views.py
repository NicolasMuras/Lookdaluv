from module_question.api.serializers.general_serializers import QuestionModuleStatisticsSerializer

from modules.api.views.modules_viewsets import ModuleViewSet



class QuestionModuleStatisticsViewSet(ModuleViewSet):
    serializer_class = QuestionModuleStatisticsSerializer

    model_to_format = QuestionModuleStatisticsSerializer.Meta.model