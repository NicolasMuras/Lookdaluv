from django.contrib import admin
from replys.models import Reply, Vote



class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'vote_character', 'reply')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'reply_character', 'answer')


admin.site.register(Vote, VoteAdmin)
admin.site.register(Reply, ReplyAdmin)