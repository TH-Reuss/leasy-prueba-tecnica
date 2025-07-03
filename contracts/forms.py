from django import forms
from .models import Contract

class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'client', 
            'car', 
            'weekly_fee', 
            'total_weeks', 
            'start_date',
            'is_active',
        ]
        widgets = {
            'is_active': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aseguramos que el valor inicial del campo oculto sea True
        self.fields['is_active'].initial = True
        self.fields['is_active'].required = False

class ContractUpdateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'client', 
            'car', 
            'weekly_fee', 
            'total_weeks', 
            'start_date',
            'is_active',
        ] 