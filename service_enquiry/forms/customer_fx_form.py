from django import forms

class CustomerFXForm(forms.Form):
    CATEGORY_FX_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
    ]
    TRANSACTION_TYPE_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]

    # FX Transaction Details
    category_fx = forms.ChoiceField(
        choices=CATEGORY_FX_CHOICES,
        required=True,
        label='Category of FX',
        widget=forms.Select(attrs={'placeholder': 'Select Category of FX'})
    )
    transaction_type = forms.ChoiceField(
        choices=TRANSACTION_TYPE_CHOICES,
        required=True,
        label='Transaction Type',
        widget=forms.Select(attrs={'placeholder': 'Select Transaction Type'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        required=True,
        label='Payment Method',
        widget=forms.Select(attrs={'placeholder': 'Select Payment Method'})
    )
    transaction_number = forms.CharField(
        max_length=50,
        required=True,
        label='Transaction Number',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Transaction Number'})
    )

    # Sender Information
    sender_title = forms.CharField(
        max_length=50,
        required=True,
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Title'})
    )
    sender_surname = forms.CharField(
        max_length=50,
        required=True,
        label='Surname',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Surname'})
    )
    sender_first_name = forms.CharField(
        max_length=50,
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'})
    )
    sender_other_names = forms.CharField(
        max_length=50,
        required=False,
        label='Other Names',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Other Names'})
    )
    sender_address = forms.CharField(
        max_length=255,
        required=True,
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Address'})
    )
    sender_email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'})
    )
    sender_amount_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        required=True,
        label='Amount',
        widget=forms.Select(attrs={'placeholder': 'Select Currency'})
    )
    sender_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Amount'})
    )

    # Receiver Information
    receiver_title = forms.CharField(
        max_length=50,
        required=True,
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Title'})
    )
    receiver_surname = forms.CharField(
        max_length=50,
        required=True,
        label='Surname',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Surname'})
    )
    receiver_first_name = forms.CharField(
        max_length=50,
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'})
    )
    receiver_other_names = forms.CharField(
        max_length=50,
        required=False,
        label='Other Names',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Other Names'})
    )
    receiver_address = forms.CharField(
        max_length=255,
        required=True,
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Address'})
    )
    receiver_email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'})
    )
    receiver_postal_code = forms.CharField(
        max_length=20,
        required=True,
        label='Postal Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Postal Code'})
    )
    receiver_bank_address = forms.CharField(
        max_length=255,
        required=True,
        label='Bank Address',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Bank Address'})
    )
    receiver_account_number = forms.IntegerField(
        max_length=50,
        required=True,
        label='Account Number',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Account Number'})
    )
    receiver_iban = forms.CharField(
        max_length=50,
        required=True,
        label='IBAN',
        widget=forms.TextInput(attrs={'placeholder': 'Enter IBAN'})
    )
    receiver_amount_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        required=True,
        label='Amount Currency',
        widget=forms.Select(attrs={'placeholder': 'Select Currency'})
    )
    receiver_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        label='Amount Received',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Amount'})
    )
    transfer_reason = forms.CharField(
        max_length=255,
        required=True,
        label='Transfer Reason',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Transfer Reason'})
    )

    def __init__(self, *args, **kwargs):
        super(CustomerFXForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'