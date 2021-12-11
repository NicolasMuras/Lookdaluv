from django.contrib import admin
from module_question.models import QuestionModule, QuestionModuleStatistics



class QuestionModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficult', 'level_steps')


class QuestionModuleStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'completed', 'max_step_reached', 'value_generated')

admin.site.register(QuestionModule, QuestionModuleAdmin)
admin.site.register(QuestionModuleStatistics, QuestionModuleStatisticsAdmin)