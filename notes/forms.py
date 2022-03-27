from django import forms
from django.core.exceptions import ValidationError

from .models import Notes
position_strength = [
    ('-2', 'Strongly Disagree'),
    ('-1', 'Disagree'),
    ('0', 'Neutral'),
    ('1', 'Agree'),
    ('2', 'Strongly Agree'),
    ]

class NotesForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'guns', 'knives')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"}),
            'guns': forms.RadioSelect(choices=position_strength),
            'knives': forms.RadioSelect(choices=position_strength)
        }
        labels = {
            'text': 'Write your thoughts here:',
            'guns': 'Do you support gun control'
        }



