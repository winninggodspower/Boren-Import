
from django.contrib import messages

from .models import Newsletter

# Create your views here.
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Perform validation
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        # Validate email format
        try:
            validate_email(email)
        except ValidationError as e:
            return JsonResponse({'error': 'Please enter a valid email address.'}, status=400)

        # Check if email is already subscribed
        if Newsletter.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email is already subscribed'}, status=400)

        # subscribe email to newsletter
        Newsletter.objects.create(email=email)
        return JsonResponse({'success': 'Subscribed successfully'})

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

