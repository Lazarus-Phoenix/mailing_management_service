from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Message

class MessageListView(ListView):
    model = Message
    template_name = 'mailing_messages/message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing_messages/message_detail.html'
    context_object_name = 'message'

class CreateMessageView(CreateView):
    model = Message
    fields = ['subject', 'body']
    template_name = 'mailing_messages/create_message.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)