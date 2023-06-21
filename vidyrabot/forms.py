from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'full_text', 'summ_uslug']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия, Имя, Отчество'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст обращения'
            }),
            "summ_uslug": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес, телефон'
            }),
        }
