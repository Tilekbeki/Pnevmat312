from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Профили'

    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.username
