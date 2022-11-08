from django.forms import ModelForm
from django import forms
from .models import Notes

class NotesForm(ModelForm):

    class Meta:
        model = Notes
        fields = ['name', 'descriptions', 'important']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 30}),
        }