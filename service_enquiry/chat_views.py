import json
import time
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from service_enquiry.models.chat_models import Message, ChatRoom

from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

from service_enquiry.models.customer_fx_model import CustomerFX
from service_enquiry.models.procurement_model import Procurement


def create_chat_room_for_form(form_id, form_type):
    if form_type == 'procurement':
        form = get_object_or_404(Procurement, id=form_id)
    elif form_type == 'customerfx':
        form = get_object_or_404(CustomerFX, id=form_id)
    else:
        raise ValueError('Invalid form type')

    form_type_id = ContentType.objects.get_for_model(form.__class__).id
    chat_room, created = ChatRoom.objects.get_or_create(form_type_id=form_type_id, form_id=form.id)
    return chat_room

def fetch_messages(request, chat_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_id)
    messages = Message.objects.filter(chat_room=chat_room).order_by('sent_at')
    messages_data = [
        {'content': msg.content, 'sender': msg.sender.email, 'sent_at': msg.sent_at.isoformat(), 'sender_is_staff': msg.sender.is_staff}
        for msg in messages
    ]
    return JsonResponse({'messages': messages_data})


@csrf_exempt
def send_message(request, chat_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        chat_room = get_object_or_404(ChatRoom, id=chat_id)
        Message.objects.create(
            chat_room=chat_room,
            sender=request.user,
            content=data['content']
        )
        return HttpResponse(status=204)
    return HttpResponse(status=405)


def stream_messages(request, chat_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_id)

    def event_stream():
        last_message_time = timezone.now()
        while True:
            messages = Message.objects.filter(chat_room=chat_room, sent_at__gt=last_message_time).order_by('sent_at')
            for message in messages:
                last_message_time = message.sent_at
                yield f"data: {json.dumps({'content': message.content, 'sender': message.sender.email, 'sent_at': message.sent_at.isoformat()})}\n\n"
            time.sleep(1)  # Wait for 1 second before checking for new messages

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
