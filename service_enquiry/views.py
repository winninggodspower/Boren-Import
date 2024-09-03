from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse

from service_enquiry.chat_views import create_chat_room_for_form
from service_enquiry.forms.customer_fx_form import CustomerFXForm
from service_enquiry.forms.risk_attestation_form import RiskAttestationForm
from .forms.procurement_form import ProcurementForm

# Create your views here.

def procurement_form(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to log in to submit the form.')
            login_url = reverse('login')  
            redirect_url = f"{login_url}?next={request.path}"
            return redirect(redirect_url)
        
        form = ProcurementForm(request.POST)
        if form.is_valid():
            messages.error(request, 'Successfuly submited procurement form. our team will get back to you')
            procurement_instance = form.save(commit=False)
            procurement_instance.user = request.user
            procurement_instance.save()

            # create chat room
            create_chat_room_for_form(procurement_instance.id, 'procurement')
            
            return redirect('/')  # Replace 'success_url' with your actual success URL
    else:
        form = ProcurementForm()

    return render(request, 'services_forms/procurement_form.html', {'form': form})

def customer_fx_form(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to log in to submit the form.')
            login_url = reverse('login')  
            redirect_url = f"{login_url}?next={request.path}"
            return redirect(redirect_url)
        
        form = CustomerFXForm(request.POST)

        if form.is_valid():
            messages.error(request, 'Successfuly submited fx form. our team will get back to you')
            fx_instance = form.save(commit=False)
            fx_instance.user = request.user
            fx_instance.save()

            # create chat room
            create_chat_room_for_form(fx_instance.id, 'customerfx')

            return redirect('/')  # Replace to home

    else:
        form = CustomerFXForm()

    return render(request, 'services_forms/customer_fx_form.html', {'form': form})


def risk_attestation_form(request):
    if request.method == 'POST':
        form = RiskAttestationForm(request.POST)

        if form.is_valid():
            messages.error(request, 'Successfuly submited risk attestation form. our team will get back to you')
            form.save()
            return redirect('/')

    else:
        form = RiskAttestationForm()

    return render(request, 'services_forms/risk_attestation_form.html', {'form': form})