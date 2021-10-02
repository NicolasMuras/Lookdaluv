from django.contrib import admin
from cards.models import Card, Module

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_type')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'card_module', 'rarity')

admin.site.register(Module, ModuleAdmin)
admin.site.register(Card, CardAdmin)