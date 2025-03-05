from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView,
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,
    HomeView, MailingReportView, start_mailing, MailingAttemptListView
)

urlpatterns = [
    path('', cache_page(60 * 15)(HomeView.as_view()), name='home'),
    # Clients URLs
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    # Mailings URLs
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('report/', MailingReportView.as_view(), name='mailing-report'),
    path('mailing/<int:pk>/start/', start_mailing, name='mailing-start'),

    # Messages URLs
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('attempts/', MailingAttemptListView.as_view(), name='attempt-list'),


]
