from django.core import checks
from django.contrib.staticfiles.finders import find

from .apps import RemindersConfig

@checks.register()
def voice_reminders_exist(app_configs, **kwargs):
    for x, _ in RemindersConfig.voice_reminders:
        if not find(x):
            yield checks.Error(
                "Reminder recording missing: %r" % x,
                id='takeyourmeds.reminders.E001',
            )
