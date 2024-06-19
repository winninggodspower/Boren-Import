from django.shortcuts import render

# Create your views here.

#services views
def fx_payment(request):
    return render(request, 'services/fx_payment.html')

def air_shipping(request):
    return render(request, 'services/air_shipping.html')

def goods_procurement(request):
    return render(request, 'services/goods_procurement.html')

def product_consultation(request):
    return render(request, 'services/product_consultation.html')

def product_sourcing(request):
    return render(request, 'services/product_sourcing.html')

def sea_shipping(request):
    return render(request, 'services/sea_shipping.html')