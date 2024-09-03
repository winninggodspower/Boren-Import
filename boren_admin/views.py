from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from service_enquiry.models import Procurement, CustomerFX
from django.contrib import messages

# Create your views here.

def submitted_forms(request):
    if not request.user.is_superuser:
        messages.error(request, 'you don\'t have permissions to access this page')
        return redirect(reverse('login'))
    
    procurements = Procurement.objects.all()
    fxs = CustomerFX.objects.all()

    context = {
        "procurement_forms": procurements,
        "fx_forms": fxs,
    }

    return render(request, "admins/admin_submitted_forms.html", context)

def procurement_form_detail(request, form_id):
    form_detail = get_object_or_404(Procurement, id=form_id)
    context = {
        "is_procurement": True,
        "detail": form_detail,
    }
    return render(request, "admins/form_details.html", context)

def fx_form_detail(request, form_id):
    form_detail = get_object_or_404(CustomerFX, id=form_id)
    context = {
        "is_procurement": False,
        "detail": form_detail,
    }
    return render(request, "admins/form_details.html", context)
