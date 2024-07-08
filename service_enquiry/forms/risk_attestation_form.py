from django import forms
from ..models import RiskAttestation

class RiskAttestationForm(forms.ModelForm):
    class Meta:
        model = RiskAttestation
        fields = [
            'person_name', 'person_address', 'person_landmark', 'person_phone',
            'guarantor_name', 'guarantor_address', 'guarantor_landmark', 'guarantor_phone',
            'supplier_name', 'supplier_address', 'supplier_phone', 'amount_currency', 'amount_to_pay'
        ]
        widgets = {
            'person_name': forms.TextInput(attrs={'placeholder': 'Enter the name of the person'}),
            'person_address': forms.Textarea(attrs={'placeholder': 'Enter the address of the person', 'class': 'form-textarea'}),
            'person_landmark': forms.TextInput(attrs={'placeholder': 'Enter the nearest landmark'}),
            'person_phone': forms.NumberInput(attrs={'placeholder': 'Enter the phone number'}),
            'guarantor_name': forms.TextInput(attrs={'placeholder': 'Enter the name of the guarantor'}),
            'guarantor_address': forms.Textarea(attrs={'placeholder': 'Enter the address of the guarantor', 'class': 'form-textarea'}),
            'guarantor_landmark': forms.TextInput(attrs={'placeholder': 'Enter the nearest landmark'}),
            'guarantor_phone': forms.NumberInput(attrs={'placeholder': 'Enter the phone number'}),
            'supplier_name': forms.TextInput(attrs={'placeholder': 'Enter the name of the supplier/company'}),
            'supplier_address': forms.Textarea(attrs={'placeholder': 'Enter the address of the supplier/company', 'class': 'form-textarea'}),
            'supplier_phone': forms.NumberInput(attrs={'placeholder': 'Enter the phone number'}),
            'amount_currency': forms.Select(attrs={'placeholder': 'Select Currency'}),
            'amount_to_pay': forms.TextInput(attrs={'placeholder': 'Enter the amount to be paid'}),
        }

    def __init__(self, *args, **kwargs):
        super(RiskAttestationForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'
