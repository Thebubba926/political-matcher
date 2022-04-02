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
            'knives': forms.RadioSelect(choices=position_strength),
            'Abortion': forms.RadioSelect(choices=position_strength),
            'MarijuanaMed': forms.RadioSelect(choices=position_strength),
            'MarijuanaRec': forms.RadioSelect(choices=position_strength),
            'VoterFraud': forms.RadioSelect(choices=position_strength),
            'WealthyTax': forms.RadioSelect(choices=position_strength)
        }
        labels = {
            'text': 'Write your thoughts here:',
            'guns': 'Do you support gun control',
            'knives': 'Do you support knife control',
            'Abortion': 'Abortion should be illegal under any circumstace',
            'MarijuanaMed': 'Marijuana should be legalized for Medical use',
            'MarijuanaRec': 'Marijuana should be legalized for recreational use',
            'VoterFraud': 'Voter fraud is a serious issue in our electoral system',
            'WealthyTax': 'Wealthy individuals are taxed excessively'
        }


