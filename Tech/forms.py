from django import forms
from .models import Amiibo

class AmiiboForm(forms.ModelForm):
    class Meta:
        model = Amiibo
        fields = ['id', 'name', 'series', 'is_owned', 'condition_status' ]
        # Apply CSS styles
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter name',
            }),
            'series': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Series Amiibo is from',
                }),
            'is_owned': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'condition_status': forms.Select(attrs={
                'class': 'form-control',
            }),

        }
