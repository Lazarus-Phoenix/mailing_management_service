from django.db import models
from clients.models import Client
from mailing_messages.models import Message
from users.models import CustomUser

class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)