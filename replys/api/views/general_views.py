from replys.api.serializers.general_serializers import VoteSerializer

from modules.api.views.general_views import GeneralViewSet



class VoteViewSet(GeneralViewSet):
    serializer_class = VoteSerializer

    model_to_format = VoteSerializer.Meta.model
