from django.db import models
from users.models import CustomUser


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} ({self.email})"  # Отображает строково имя и email

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject  # Отображает строково тему сообщения

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
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