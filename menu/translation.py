from modeltranslation.translator import register, TranslationOptions
from .models import Menu
#Переклад моделей
@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)