from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, BaseModel):
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'