from django.urls import path
from .views import MailingListView, MailingCreateView

app_name = 'mailings'

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', MailingUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
]