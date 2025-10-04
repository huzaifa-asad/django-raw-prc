from django.apps import AppConfig


class BlogsignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogSignals'
    
    def ready(self):
        import blogSignals.signals
