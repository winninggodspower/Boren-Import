from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from blog.models import BlogIndexPage
from core.models import Gallery
from service_enquiry.models.chat_models import ChatRoom
from service_enquiry.models.customer_fx_model import CustomerFX
from service_enquiry.models.procurement_model import Procurement

# Create your views here.
def home(request):
    blogs = BlogIndexPage.objects.first().get_children()
    gallery = Gallery.objects.all()

    context = {
        'galleries': gallery,
        'blogs': blogs,
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

@login_required
def profile_dashbard(request):
    user_procurements = Procurement.objects.filter(user=request.user)
    user_fxs = CustomerFX.objects.filter(user=request.user)

    # Get the ContentType for Procurement and CustomerFX models
    procurement_content_type = ContentType.objects.get_for_model(Procurement)
    fx_content_type = ContentType.objects.get_for_model(CustomerFX)

    # Create a dictionary of chat rooms mapped by form_id
    procurement_chat_rooms = {
        chat_room.form_id: chat_room
        for chat_room in ChatRoom.objects.filter(
            form_type=procurement_content_type,
            form_id__in=user_procurements.values_list('id', flat=True)
        )
    }

    fx_chat_rooms = {
        chat_room.form_id: chat_room
        for chat_room in ChatRoom.objects.filter(
            form_type=fx_content_type,
            form_id__in=user_fxs.values_list('id', flat=True)
        )
    }

    context = {
        "user_procurements": user_procurements,
        "user_fxs": user_fxs,
        "procurement_chat_rooms": procurement_chat_rooms,
        "fx_chat_rooms": fx_chat_rooms,
    }

    return render(request, 'profile_dashboard.html', context)
