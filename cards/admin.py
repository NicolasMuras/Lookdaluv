from django.contrib import admin
from cards.models import Card



class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_module', 'rarity')

admin.site.register(Card, CardAdmin)