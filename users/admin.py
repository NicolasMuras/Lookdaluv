from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile, ProfileStatistics



class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_admin', 'is_active', 'date_joined', 'last_login', 'profile_image')

    fieldsets = (
        (None, {'fields': ('username', 'email','password')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'age', 'nationality', 'subscription_end_date')


class ProfileStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'interview_simulator_completed', 'workflow_completed', 'deconstructor_completed', 'portfolio_booster_completed')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileStatistics, ProfileStatisticsAdmin)