from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    social_id = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=20)
    provider = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)