from django.urls import path
from .views import ClientListView, ClientCreateView

app_name = 'mailing'

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', MailingUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
]