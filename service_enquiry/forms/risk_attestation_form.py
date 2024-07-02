from django import forms

class RiskAttestationForm(forms.Form):
    # Personal Information
    person_name = forms.CharField(
        label='Name of Person', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of the person',
        })
    )
    person_address = forms.CharField(
        label='Address', 
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter the address of the person',
            'class': 'form-textarea'
        })
    )
    person_landmark = forms.CharField(
        label='Nearest Landmark', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the nearest landmark',
        })
    )
    person_phone = forms.CharField(
        label='Phone Number', 
        max_length=15,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter the phone number',
        })
    )

    # Guarantors Information
    guarantor_name = forms.CharField(
        label='Name of Guarantor', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of the guarantor',
        })
    )
    guarantor_address = forms.CharField(
        label='Address', 
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter the address of the guarantor',
            'class': 'form-textarea'
        })
    )
    guarantor_landmark = forms.CharField(
        label='Nearest Landmark', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the nearest landmark',
        })
    )
    guarantor_phone = forms.CharField(
        label='Phone Number', 
        max_length=15,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter the phone number',
        })
    )

    # Supplier Details
    supplier_name = forms.CharField(
        label='Name of Supplier/Company', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of the supplier/company',
        })
    )
    supplier_address = forms.CharField(
        label='Address', 
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter the address of the supplier/company',
            'class': 'form-textarea'
        })
    )
    supplier_phone = forms.CharField(
        label='Phone Number', 
        max_length=15,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter the phone number',
        })
    )
    amount_currency = forms.ChoiceField(
        label='Currency',
        choices=[('USD', 'USD'), ('EUR', 'EUR'), ('NGN', 'NGN')],
    )
    amount_to_pay = forms.DecimalField(
        label='Amount to be Paid',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the amount to be paid',
        })
    )

    def __init__(self, *args, **kwargs):
        super(RiskAttestationForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'