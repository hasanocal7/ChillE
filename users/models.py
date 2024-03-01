# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    is_member = models.BooleanField(default=True)
    is_business = models.BooleanField(blank=True, null=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"