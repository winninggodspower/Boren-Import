from django.conf import settings
from django.shortcuts import redirect, render
from .models import Tracker
import requests

# Create your views here.

def tracking(request, tracking_number):
    header = headers={'Authorization': f'Bearer {settings.SHIP24_API_KEY}'}
    response = requests.post(
        'https://api.ship24.com/public/v1/trackers/track',
        headers=header,
        data={'trackingNumber': tracking_number}
        )
    print(response.json())
    tracking_data = response.json().get('data').get('trackings')[0]

    context = {
        'tracking': tracking_data,
        'tracking_number': tracking_number,
    }

    return render(request, 'tracking.html', context)

def submit_tracking(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        if tracking_number:
            return redirect('tracking_details', tracking_number=tracking_number)
    return redirect('home')