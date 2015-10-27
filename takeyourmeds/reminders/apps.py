from django.apps import AppConfig

class RemindersConfig(AppConfig):
    name = 'takeyourmeds.reminders'

    def ready(self):
        from . import checks # NOQA
