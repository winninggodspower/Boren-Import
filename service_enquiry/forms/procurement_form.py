# forms.py

from django import forms

class ProcurementForm(forms.Form):
    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
    ]
    CUSTOMER_TYPE_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, 
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Select Category'})
    )
    customer_type = forms.ChoiceField(
        choices=CUSTOMER_TYPE_CHOICES, 
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Select customer type'})
    )
    payment_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES, 
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Select Currency'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES, 
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Select payment method'})
    )
    purchase_order_name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Purchase Order Name'})
    )
    phone_number = forms.IntegerField(
        max_value=15, 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Phone Number',})
    )

    title = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Title'})
    )
    surname = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Surname'})
    )
    first_name = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'})
    )
    other_names = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Other Names'})
    )
    address = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter full address'})
    )
    nearest_landmark = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter nearest landmark'})
    )
    type_of_order = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Type of Order'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email address'})
    )
    social_media = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Select Social Media'})
    )
    social_media_handle = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Social Media Handle'})
    )

    recipient_name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Recipient’s Name'})
    )
    business_name = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Business Name'})
    )
    mailing_address = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter full address'})
    )
    state = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Select State'})
    )
    zip_code = forms.CharField(
        max_length=10, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Zip Code'})
    )
    mailing_phone_number = forms.IntegerField(
        max_value=15, 
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Phone Number',})
    )
    agree = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'bg-[#EFF0F2] mt-1'
        })
    )

    def __init__(self, *args, **kwargs):
        super(ProcurementForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            attriutes = visible_field.field.widget.attrs.get('class')
            if not attriutes or attriutes.strip() == '':
                visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'