from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('volunteer', 'Volunteer'),
        ('officer', 'Officer'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.username