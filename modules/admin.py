from django.contrib import admin
from modules.models import Module



class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'module_type', 'level')

admin.site.register(Module, ModuleAdmin)