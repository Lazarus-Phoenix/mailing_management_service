from django.contrib import admin
from .models import MailingAttempt

@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'status', 'attempt_time')
    readonly_fields = ('attempt_time',)
    list_filter = ('status',)