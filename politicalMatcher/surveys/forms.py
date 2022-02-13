from django import forms
from django.core.exceptions import ValidationError

from .models import Surveys

class SurveysForm(forms.ModelForm):
    class Meta:
        model = Surveys
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'text': 'Write your thoughts here:'
        }