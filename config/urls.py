from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Пути для пользовательского приложения
    path('', include('users.urls')),
    path('mailing/', include('mailing.urls')),


]