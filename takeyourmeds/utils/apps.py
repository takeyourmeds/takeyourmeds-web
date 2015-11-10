from django.apps import AppConfig

class UtilsConfig(AppConfig):
    name = 'takeyourmeds.utils'

    def ready(self):
        from . import checks # NOQA
