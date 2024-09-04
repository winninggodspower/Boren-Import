from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.contenttypes.models import ContentType

from django.urls import reverse
from service_enquiry.models import Procurement, CustomerFX
from django.contrib import messages

from service_enquiry.models.chat_models import ChatRoom

# Create your views here.

def submitted_forms(request):
    if not request.user.is_superuser:
        messages.error(request, 'you don\'t have permissions to access this page')
        return redirect(reverse('login'))
    
    procurements = Procurement.objects.all()
    fxs = CustomerFX.objects.all()

    # Get the ContentType for Procurement and CustomerFX models
    procurement_content_type = ContentType.objects.get_for_model(Procurement)
    fx_content_type = ContentType.objects.get_for_model(CustomerFX)

    # Create a dictionary of chat rooms mapped by form_id
    procurement_chat_rooms = {
        chat_room.form_id: chat_room
        for chat_room in ChatRoom.objects.filter(
            form_type=procurement_content_type,
            form_id__in=procurements.values_list('id', flat=True)
        )
    }

    fx_chat_rooms = {
        chat_room.form_id: chat_room
        for chat_room in ChatRoom.objects.filter(
            form_type=fx_content_type,
            form_id__in=fxs.values_list('id', flat=True)
        )
    }

    context = {
        "user_procurements": procurements,
        "user_fxs": fxs,
        "procurement_chat_rooms": procurement_chat_rooms,
        "fx_chat_rooms": fx_chat_rooms,
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
