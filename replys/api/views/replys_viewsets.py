from replys.api.serializers.replys_serializers import ReplySerializer

from modules.api.views.general_views import GeneralViewSet



class ReplyViewSet(GeneralViewSet):
    serializer_class = ReplySerializer

    model_to_format = ReplySerializer.Meta.model
