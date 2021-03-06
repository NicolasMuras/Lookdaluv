from django.contrib import admin
from answers.models import Answer



class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'answer_category', 'question_module')

admin.site.register(Answer, AnswerAdmin)