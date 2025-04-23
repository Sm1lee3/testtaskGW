from modeltranslation.translator import register, TranslationOptions
from .models import Menu

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)