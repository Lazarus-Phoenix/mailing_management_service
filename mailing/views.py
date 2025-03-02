from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy


from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from .forms import ClientForm, MessageForm, MailingForm
from .models import Client, Mailing, Message
from .permissions import IsOwnerMixin
from .permissions import IsOwnerFilterMixin

# Clients Views
class ClientListView(IsOwnerFilterMixin, ListView):
    model = Client
    template_name = 'mailing/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(IsOwnerFilterMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(IsOwnerMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
    template_name = 'mailing/client_confirm_delete.html'

# Mailings Views
class MailingListView(IsOwnerFilterMixin, ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'
    context_object_name = 'mailings'
    # def get_queryset(self):
    #     return Mailing.objects.filter(owner=self.request.user)

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MailingUpdateView(IsOwnerMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing_list')

class MailingDeleteView(IsOwnerMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_list')
    template_name = 'mailing/mailing_confirm_delete.html'

# Messages Views
class MessageListView(IsOwnerFilterMixin, ListView):
    model = Message
    template_name = 'mailing/message_list.html'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MessageUpdateView(IsOwnerMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(IsOwnerMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')
    template_name = 'mailing/message_confirm_delete.html'




class HomeView(TemplateView):
    """Объекты считывающие с базы кол-во рассылок и клиентов с сортингом по признакам"""
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='started').count()
        context['unique_clients'] = Client.objects.distinct().count()

        return context

