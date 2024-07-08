from django import forms
from ..models import CustomerFX

class CustomerFXForm(forms.ModelForm):
    class Meta:
        model = CustomerFX
        fields = [
            'category_fx', 'transaction_type', 'payment_method', 'transaction_number',
            'sender_title', 'sender_surname', 'sender_first_name', 'sender_other_names',
            'sender_address', 'sender_email', 'sender_amount_currency', 'sender_amount',
            'receiver_title', 'receiver_surname', 'receiver_first_name', 'receiver_other_names',
            'receiver_address', 'receiver_email', 'receiver_postal_code', 'receiver_bank_address',
            'receiver_account_number', 'receiver_iban', 'receiver_amount_currency',
            'receiver_amount', 'transfer_reason'
        ]
        widgets = {
            'category_fx': forms.Select(attrs={'placeholder': 'Select Category of FX'}),
            'transaction_type': forms.Select(attrs={'placeholder': 'Select Transaction Type'}),
            'payment_method': forms.Select(attrs={'placeholder': 'Select Payment Method'}),
            'transaction_number': forms.NumberInput(attrs={'placeholder': 'Enter Transaction Number'}),
            'sender_title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'sender_surname': forms.TextInput(attrs={'placeholder': 'Enter Surname'}),
            'sender_first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'sender_other_names': forms.TextInput(attrs={'placeholder': 'Enter Other Names'}),
            'sender_address': forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'sender_email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'sender_amount_currency': forms.Select(attrs={'placeholder': 'Select Currency'}),
            'sender_amount': forms.TextInput(attrs={'placeholder': 'Enter Amount'}),
            'receiver_title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'receiver_surname': forms.TextInput(attrs={'placeholder': 'Enter Surname'}),
            'receiver_first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'receiver_other_names': forms.TextInput(attrs={'placeholder': 'Enter Other Names'}),
            'receiver_address': forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'receiver_email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'receiver_postal_code': forms.TextInput(attrs={'placeholder': 'Enter Postal Code'}),
            'receiver_bank_address': forms.TextInput(attrs={'placeholder': 'Enter Bank Address'}),
            'receiver_account_number': forms.NumberInput(attrs={'placeholder': 'Enter Account Number'}),
            'receiver_iban': forms.TextInput(attrs={'placeholder': 'Enter IBAN'}),
            'receiver_amount_currency': forms.Select(attrs={'placeholder': 'Select Currency'}),
            'receiver_amount': forms.TextInput(attrs={'placeholder': 'Enter Amount'}),
            'transfer_reason': forms.TextInput(attrs={'placeholder': 'Enter Transfer Reason'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerFXForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'
