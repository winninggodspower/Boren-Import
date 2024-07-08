from django import forms
from ..models import Procurement

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = [
            'category', 'customer_type', 'payment_currency', 'payment_method',
            'purchase_order_name', 'phone_number', 'title', 'surname', 'first_name', 'other_names',
            'address', 'nearest_landmark', 'type_of_order', 'email', 'social_media',
            'social_media_handle', 'recipient_name', 'business_name', 'mailing_address', 'state',
            'zip_code', 'mailing_phone_number', 'agree'
        ]
        widgets = {
            'category': forms.Select(attrs={'placeholder': 'Select Category'}),
            'customer_type': forms.Select(attrs={'placeholder': 'Select customer type'}),
            'payment_currency': forms.Select(attrs={'placeholder': 'Select Currency'}),
            'payment_method': forms.Select(attrs={'placeholder': 'Select payment method'}),
            'purchase_order_name': forms.TextInput(attrs={'placeholder': 'Enter Purchase Order Name'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Enter Phone Number'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter Surname'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'other_names': forms.TextInput(attrs={'placeholder': 'Enter Other Names'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter full address'}),
            'nearest_landmark': forms.TextInput(attrs={'placeholder': 'Enter nearest landmark'}),
            'type_of_order': forms.TextInput(attrs={'placeholder': 'Enter Type of Order'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email address'}),
            'social_media': forms.TextInput(attrs={'placeholder': 'Select Social Media'}),
            'social_media_handle': forms.TextInput(attrs={'placeholder': 'Enter Social Media Handle'}),
            'recipient_name': forms.TextInput(attrs={'placeholder': 'Enter Recipient’s Name'}),
            'business_name': forms.TextInput(attrs={'placeholder': 'Enter Business Name'}),
            'mailing_address': forms.TextInput(attrs={'placeholder': 'Enter full address'}),
            'state': forms.TextInput(attrs={'placeholder': 'Select State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Enter Zip Code'}),
            'mailing_phone_number': forms.NumberInput(attrs={'placeholder': 'Enter Phone Number'}),
            'agree': forms.CheckboxInput(attrs={'class': 'bg-[#EFF0F2] mt-1'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcurementForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            attributes = visible_field.field.widget.attrs.get('class')
            if not attributes or attributes.strip() == '':
                visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'