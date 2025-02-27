from django.db import models
from users.models import CustomUser

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)