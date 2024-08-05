from django.shortcuts import redirect, render

# Create your views here.

def tracking(request, tracking_id):
    print(tracking_id)
    return render(request, 'tracking.html', {'tracking_id': tracking_id})

def submit_tracking(request):
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')
        if tracking_id:
            return redirect('tracking_details', tracking_id=tracking_id)
    return redirect('home')