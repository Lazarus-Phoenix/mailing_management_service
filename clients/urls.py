from django.urls import path
from . import views

urlpatterns = [
    # Пути для управления клиентами
    path('', views.ClientListView.as_view(), name='client_list'),
    path('create/', views.CreateClientView.as_view(), name='create_client'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/edit/', views.UpdateClientView.as_view(), name='update_client'),
    path('<int:pk>/delete/', views.DeleteClientView.as_view(), name='delete_client'),
]