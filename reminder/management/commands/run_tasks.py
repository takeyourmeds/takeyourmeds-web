from django.core.management.base import BaseCommand

from reminder.models import Reminder

class Command(BaseCommand):

    def handle(self, **options):
        for reminder in Reminder.objects.all():
            if reminder.should_run():
                reminder.dispatch_task()