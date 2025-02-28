from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from django.views.generic import TemplateView
from django.core.cache import cache
from .models import Mailing, Client


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stats = cache.get('mailing_stats')
        if not stats:
            stats = {
                'total_mailings': Mailing.objects.count(),
                'active_mailings': Mailing.objects.filter(status='started').count(),
                'unique_clients': Client.objects.values('email').distinct().count()
            }
            cache.set('mailing_stats', stats, 300)

        context.update(stats)
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