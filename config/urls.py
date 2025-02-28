from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Пути для пользовательского приложения
    path('', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('mailings/', include('mailings.urls')),
    path('messages/', include('mailing_messages.urls')),  # Добавлен для messages

    # Пути для API
    path('api/v1/auth/', include('users.api.urls')),
    path('api/v1/clients/', include('clients.api.urls')),
    path('api/v1/mailings/', include('mailings.api.urls')),
    path('api/v1/messages/', include('mailing_messages.api.urls')),  # Добавлен для messages
]