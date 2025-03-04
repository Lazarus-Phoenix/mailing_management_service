from django.core.management.base import BaseCommand
from django.utils import timezone

from config.settings import DEFAULT_FROM_EMAIL
from ...models import Mailing, MailingAttempt
from ...services import send_mailing
from django.core.mail import send_mail

def send_mailing(mailing):
    for client in mailing.clients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                DEFAULT_FROM_EMAIL,  # Используйте настройку из settings.py
                [client.email],
                fail_silently=False,
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


class Command(BaseCommand):
    help = 'Send scheduled mailings'

    def handle(self, *args, **options):
        now = timezone.now()
        mailings = Mailing.objects.filter(
            start_time__lte=now,
            end_time__gte=now,
            status__in=['created', 'started']
        )
        for mailing in mailings:
            send_mailing(mailing)
            mailing.status = 'started'
            mailing.save()
