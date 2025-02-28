from django.db import models
from users.models import CustomUser


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Mailing(models.Model):
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Владелец')
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена')
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class MailingAttempt(models.Model):
    
    status = models.CharField(max_length=15, choices=[('success', 'Успешно'), ('failed', 'Не успешно')])
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts')

    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно')
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)