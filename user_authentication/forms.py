from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# import the model here to populate the form
from django.contrib.auth import get_user_model
User = get_user_model()

def validate_email(email):
    if not User.objects.filter(email = email).first():
        raise forms.ValidationError('Incorrect email or password')


def email_available(email):
    if User.objects.filter(email = email).first():
        raise forms.ValidationError('Email already taken. if yours, proceed to login')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={'placeholder':'Enter Comfirm password'}))
    class Meta:
        model = User
        # specify field to be displayed from model here
        fields = ('fullname','email','password1', 'password2', 'phone')
        widgets = { 
            'fullname': forms.TextInput(attrs={'placeholder':'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter Email Address',}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-input h-14 md:h-[3.7rem] input-border'

    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

