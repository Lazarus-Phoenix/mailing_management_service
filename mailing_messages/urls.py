from django.urls import path

from mailing_messages.views import MessageListView, CreateMessageView, MessageDetailView

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('create/', CreateMessageView.as_view(), name='create_message'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]