from django.views.generic import DetailView
from .models import Message

class MessagePreviewView(DetailView):
    model = Message
    template_name = 'mailing_messages/preview.html'
