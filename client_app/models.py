from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length= 255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
