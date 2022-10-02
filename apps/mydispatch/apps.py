from django.apps import AppConfig


class MydispatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mydispatch'

    # def ready(self):
    #     from apps.mydispatch import signals