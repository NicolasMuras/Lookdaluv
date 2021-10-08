from django.contrib import admin
from users.models import User, Profile, ProfileStatistics



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_admin', 'is_active')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'last_name', 'age', 'nationality', 'subscription_end_date')


class ProfileStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'personal_growth_completed', 'chatbot_completed', 'simpl_deconstructor_completed', 'date_simulation_completed', 'sex_arts_completed', 'environment_dominance_completed')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileStatistics, ProfileStatisticsAdmin)