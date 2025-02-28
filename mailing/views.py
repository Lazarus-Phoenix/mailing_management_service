from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from django.views.generic import TemplateView
from django.core.cache import cache
from .models import Mailing, Client
from .permissions import IsOwnerMixin

from django.views.generic import TemplateView
from .models import Mailing, Client


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='started').count()
        context['unique_clients'] = Client.objects.distinct().count()

        return context

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mailing/client_list.html'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    template_name = 'mailing/client_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(IsOwnerMixin, UpdateView):
    ...


class ClientDeleteView:
    pass


class MailingListView:
    pass


class MailingCreateView:
    pass


class MailingUpdateView:
    pass


class MailingDeleteView:
    pass