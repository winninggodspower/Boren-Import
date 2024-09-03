from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from service_enquiry.models.customer_fx_model import CustomerFX
from service_enquiry.models.procurement_model import Procurement

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile_dashbard(request):
    user_procurements = Procurement.objects.filter(user=request.user)
    user_fxs = CustomerFX.objects.filter(user=request.user)

    context = {
        "user_procurements": user_procurements,
        "user_fxs": user_fxs,
    }
    return render(request, 'profile_dashboard.html', context)
