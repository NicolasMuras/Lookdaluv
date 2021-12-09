from django.contrib import admin
from contents_interview_simulator.models import InterviewSimulatorModule, InterviewSimulatorModuleStatistics



class InterviewSimulatorModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficult', 'level_steps')


class InterviewSimulatorModuleStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'completed', 'max_step_reached', 'value_generated')

admin.site.register(InterviewSimulatorModule, InterviewSimulatorModuleAdmin)
admin.site.register(InterviewSimulatorModuleStatistics, InterviewSimulatorModuleStatisticsAdmin)