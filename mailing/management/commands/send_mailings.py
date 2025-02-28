from datetime import timezone

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailing.models import Mailing, MailingAttempt


class Command(BaseCommand):
    help = 'Send scheduled mailing'

    def handle(self, *args, **options):
        current_time = timezone.now()
        mailings = Mailing.objects.filter(
            start_time__lte=current_time,
            end_time__gte=current_time,
            status__in=['created', 'started']
        )

        for mailing in mailings:
            mailing.status = 'started'
            mailing.save()

            for client in mailing.clients.all():
                try:
                    send_mail(
                        mailing.message.subject,
                        mailing.message.body,
                        None,
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