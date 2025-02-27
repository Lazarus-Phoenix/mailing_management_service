from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Mailing
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MailingForm
from django.shortcuts import render
from .models import Mailing
from clients.models import Client

from django.contrib.auth.mixins import UserPassesTestMixin

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Менеджеры').exists()


def home(request):
    context = {
        'total_mailings': Mailing.objects.count(),
        'active_mailings': Mailing.objects.filter(status='started').count(),
        'unique_clients': Client.objects.distinct().count(),
    }
    return render(request, 'home.html', context)

class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailings/mailing_list.html'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)