from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from mailing.models import Mailing

class Command(BaseCommand):
    help = 'Создает группы и назначает права'

    def handle(self, *args, **options):
        managers_group, created = Group.objects.get_or_create(name='Менеджеры')
        view_perm = Permission.objects.get(codename='can_view_all')
        disable_perm = Permission.objects.get(codename='can_disable')
        managers_group.permissions.add(view_perm, disable_perm)
        self.stdout.write('Группа "Менеджеры" создана')