from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_vendor = models.BooleanField(default=False)

class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    mobile_number = models.CharField(max_length=20, blank=False)
    cnic = models.CharField(max_length=20, blank=False)
