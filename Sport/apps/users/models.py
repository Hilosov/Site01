from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    
    # class Meta:
    # model = CustomUser
    # fields = ("username",)

