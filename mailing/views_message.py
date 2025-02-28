from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Message
from .permissions import IsOwnerMixin

class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'

class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'body']
    template_name = 'mailing/message_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)