from users.api.serializers.general_serializers import ProfileSerializer, ProfileStatisticsSerializer

from modules.api.views.general_views import GeneralViewSet



class ProfileViewSet(GeneralViewSet):
    serializer_class = ProfileSerializer

    model_to_format = ProfileSerializer.Meta.model


class ProfileStatisticsViewSet(GeneralViewSet):
    serializer_class = ProfileStatisticsSerializer

    model_to_format = ProfileStatisticsSerializer.Meta.model