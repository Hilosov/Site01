from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class CustomUser(User):
    age = models.PositiveIntegerField(null=True, blank=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)


    
        
