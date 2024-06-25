from django.shortcuts import render

# Create your views here.

def procurement_form(request):
    return render(request, 'services_forms/procurement_form.html')