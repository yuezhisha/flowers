from django.apps import AppConfig
from .mqtt import mqtt_client

class AiserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AIServer'
    def ready(self):
        mqtt_client.loop_start()