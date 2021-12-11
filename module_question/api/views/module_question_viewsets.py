from module_question.api.serializers.module_question_serializers import QuestionModuleSerializer

from modules.api.views.general_views import GeneralViewSet



class QuestionModuleViewSet(GeneralViewSet):
    serializer_class = QuestionModuleSerializer

    model_to_format = QuestionModuleSerializer.Meta.model
