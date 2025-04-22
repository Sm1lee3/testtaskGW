from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(models.Menu)
class MenuAdmin(TranslationAdmin):
    list_display = ('name',)