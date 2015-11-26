from django.apps import AppConfig

class RemindersConfig(AppConfig):
    name = 'takeyourmeds.reminders'

    voice_reminders = (
        (
            'mp3/hi_mum_medication_reminder.mp3',
            "Mum's medication reminder!",
        ),
        (
            'mp3/its_fiona_mouthwash_reminder.mp3',
            "Dental Hygienist",
        ),
    )

    def ready(self):
        from . import checks #pylint: disable=unused-variable
