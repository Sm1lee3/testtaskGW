from django.forms import ModelForm, TextInput, Select
from .models import Menu
#Форма для маніпуляцій з пунктами меню
class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['name_uk','name_en', 'parent']
        widgets = {
            'name_uk': TextInput(attrs={'placeholder': 'Enter menu name', 'required': True}),
            'name_en': TextInput(attrs={'placeholder': 'Enter menu name', 'required': True}),
            'parent': Select(attrs={'class': 'form-control'}),
        }