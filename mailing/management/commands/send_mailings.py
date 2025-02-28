from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Mailing
from ...services import send_mailing

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