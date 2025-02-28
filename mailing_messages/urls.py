from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view(), name='message_list'),
    path('create/', views.CreateMessageView.as_view(), name='create_message'),
    path('<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]