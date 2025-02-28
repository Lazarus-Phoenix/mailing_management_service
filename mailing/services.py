from django.core.mail import send_mail
from .models import MailingAttempt

def send_mailing(mailing):
    for client in mailing.clients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                None,  # Использовать EMAIL_HOST_USER из settings
                [client.email],
                fail_silently=False
            )
            MailingAttempt.objects.create(
                status='success',
                mailing=mailing
            )
        except Exception as e:
            MailingAttempt.objects.create(
                status='failed',
                server_response=str(e),
                mailing=mailing
            )