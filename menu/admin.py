from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin
#Реєстрація в панелі адміна модделі меню
@admin.register(models.Menu)
class MenuAdmin(TranslationAdmin):
    list_display = ('name',)