from django.apps import AppConfig


class CustomTaskConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "custom_task"

    def ready(self) -> None:
        import custom_task.signals