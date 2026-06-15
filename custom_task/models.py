from django.contrib.auth.models import User
from django.db import models


class UpperCaseField(models.CharField):
    def get_prep_value(self, value:str) -> str:
        """getting prepared value for returning the upper case value"""
        value = super().get_prep_value(value)
        if isinstance(value, str):
            return value.upper()
        return value    


class UserConfig(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="config"
    )
    phone_number = models.CharField(max_length=15, blank=True)
    settings = models.JSONField(default=dict, blank=True)
    bio = UpperCaseField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        """a saving alhorythm"""
        super().save(*args, **kwargs)

    def get_total_amount_of_settings(self) -> int:
        """getting total amount of settings"""
        return len(self.settings)

    def __str__(self) -> str:
        return self.user.username


class UserLog(models.Model):
    user_config = models.ForeignKey(
        UserConfig, on_delete=models.CASCADE, related_name="logs"
    )
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True) 