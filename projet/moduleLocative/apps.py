from django.apps import AppConfig


class ModulelocativeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moduleLocative'
    
    def ready(self) :
        import moduleLocative.signals
