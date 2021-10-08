from django.contrib import admin
from contents_chatbot.models import ChatbotModule, ChatbotModuleStatistics



class ChatbotModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficult', 'level_steps')


class ChatbotModuleStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'completed', 'max_step_reached', 'value_generated', 'romance_generated')

admin.site.register(ChatbotModule, ChatbotModuleAdmin)
admin.site.register(ChatbotModuleStatistics, ChatbotModuleStatisticsAdmin)