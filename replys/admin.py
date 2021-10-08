from django.contrib import admin
from replys.models import Reply



class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'reply_character', 'answer')

admin.site.register(Reply, ReplyAdmin)