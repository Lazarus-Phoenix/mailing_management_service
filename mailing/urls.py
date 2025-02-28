from django.urls import path
from .views import (
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView,
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]