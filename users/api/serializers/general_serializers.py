from rest_framework import serializers

from users.models import Profile, ProfileStatistics, User



class ProfileStatisticsSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = ProfileStatistics
        fields = [
            'id',
            'profile',
            'question_completed', 
            'workflow_completed',
            'deconstructor_completed',
            'image_comparision_completed',]
 
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


class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

    def validate(self, attrs):

        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})

        username = attrs.get('username', '')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('Username is already in use')})

        return super().validate(attrs)

    def create(self, validated_data):

        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        username = validated_data.get('username', '')
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')
        nationality = "es-es"
        user = User.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.save()

        return Profile.objects.create(user=user, first_name=first_name, last_name=last_name, nationality=nationality)