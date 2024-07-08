from django.shortcuts import render, redirect
from django.contrib import messages

from service_enquiry.forms.customer_fx_form import CustomerFXForm
from service_enquiry.forms.risk_attestation_form import RiskAttestationForm
from .forms.procurement_form import ProcurementForm

# Create your views here.

def procurement_form(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            messages.error(request, 'Successfuly submited procurement form. our team will get back to you')
            form.save()
            return redirect('/')  # Replace 'success_url' with your actual success URL
    else:
        form = ProcurementForm()

    return render(request, 'services_forms/procurement_form.html', {'form': form})

def customer_fx_form(request):
    if request.method == 'POST':
        form = CustomerFXForm(request.POST)

        if form.is_valid():
            messages.error(request, 'Successfuly submited fx form. our team will get back to you')
            form.save()
            return redirect('/')  # Replace 'success_url' with your actual success URL

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