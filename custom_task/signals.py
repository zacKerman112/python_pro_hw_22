from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserConfig, UserLog


@receiver(post_save, sender=UserConfig)
def log_user_config_save(sender, instance, created, **kwargs) -> None:
    """Saving user configuration to the logger file."""
    if created:
        UserLog.objects.create(
            user_config=instance, action="Config Profile Created"
        )
    else:
        UserLog.objects.create(
            user_config=instance, action="Config Profile Updated"
        )