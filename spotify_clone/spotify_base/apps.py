from django.apps import AppConfig


class SpotifyBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spotify_base'

    def ready(self):
        import spotify_base.signals
