from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# modules needed for user authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#for pasword reset
from django.contrib.auth import views
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.conf import settings

# importing the use model
from django.contrib.auth import get_user_model
User = get_user_model()


# importing the forms
from .forms import LoginForm, RegisterForm

# Create your views here.

# routes for user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # form.save only works when form is created from a model
            form.save()
            messages.success(request, 'succesfully created account')
            return redirect('login')
        else:
            # rendering the template again if the form is not valid with the prepopulated data.
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_user(request):
    # redirect user to home if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You Are Already Logged In')
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'successfully logged in as {user.email}')
                return redirect(request.GET.get('next', '/'))
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')

        # if form is not valid render the template again with pre populated data
        else:
            print('invalid form')
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



@login_required
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'successfully logged out')
        return redirect('/')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    email_content = {
                    "email":user.email,
                    'domain': settings.DOMAIN,
                    'site_name': settings.SITE_NAME,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': settings.PROTOCOL,
                    }
                    email = render_to_string(email_template_name, email_content)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
            else:
                messages.error(request, 'email not found in our database')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
