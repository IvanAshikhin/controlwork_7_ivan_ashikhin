from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    name = forms.CharField(max_length=500, required=True, label="Имя")
    email = forms.EmailField(max_length=500, required=True, label='Почта')
    text = forms.CharField(max_length=500, required=True, label='Описание', widget=widgets.Textarea)