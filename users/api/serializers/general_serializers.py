from rest_framework import serializers

from users.models import Profile, ProfileStatistics



class ProfileStatisticsSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = ProfileStatistics
        fields = [
            'id',
            'profile',
            'personal_growth_completed', 
            'chatbot_completed',
            'simpl_deconstructor_completed',
            'date_simulation_completed',
            'sex_arts_completed',
            'environment_dominance_completed',]
 
    def get_profile(self, instance):
        return instance.__str__()


class ProfileSerializer(serializers.ModelSerializer):

    profilestatistics = ProfileStatisticsSerializer(many=True, read_only=True)
    rank = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'last_name', 'age', 'nationality', 'subscription_end_date', 'level', 'rank', 'language']
 
    def get_rank(self, instance):
        return instance.get_rank_display()

    def get_language(self, instance):
        return instance.get_language_display()

