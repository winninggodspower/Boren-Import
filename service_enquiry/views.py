from django.shortcuts import render, redirect

from service_enquiry.forms.customer_fx_form import CustomerFXForm
from .forms.procurement_form import ProcurementForm

# Create your views here.

def procurement_form(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # For example, save it to the database
            # ...

            return redirect('success_url')  # Replace 'success_url' with your actual success URL
    else:
        form = ProcurementForm()

    return render(request, 'services_forms/procurement_form.html', {'form': form})

def customer_fx_form(request):
    if request.method == 'POST':
        form = CustomerFXForm(request.POST)

        if form.is_valid():
            # Handle form data
            return redirect('success')

    else:
        form = CustomerFXForm()

    return render(request, 'services_forms/customer_fx_form.html', {'form': form})