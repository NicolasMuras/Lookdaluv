from answers.api.serializers.answers_serializers import AnswerSerializer

from modules.api.views.general_views import GeneralViewSet



class AnswerViewSet(GeneralViewSet):
    serializer_class = AnswerSerializer

    model_to_format = AnswerSerializer.Meta.model
