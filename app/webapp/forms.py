from django import forms
from .models import GuestBook


class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['name', 'email', 'text']
        labels = {
            'name': 'Имя',
            'email': 'Почта',
            'text': 'Описание'
        }
        widgets = {
            'text': forms.Textarea()
        }
