from django.core.management.base import BaseCommand

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
                status="success",
                mailing=mailing,
                server_response="Сообщение успешно отправлено",
            )
        except Exception as e:
            MailingAttempt.objects.create(
                status="failed",
                mailing=mailing,
                server_response=str(e),
            )


class Command(BaseCommand):
    help = "Send scheduled mailings"

    def handle(self, *args, **options):
        mailings = Mailing.objects.filter(status="started")
        for mailing in mailings:
            send_mailing(mailing)
            mailing.status = "started"
            mailing.save()


# class Command(BaseCommand):
#     help = 'Send mailings'
#
#     def handle(self, *args, **options):
#         mailings = Mailing.objects.filter(status='started')
#         for mailing in mailings:
#             send_mailing(mailing)
