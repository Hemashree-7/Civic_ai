from django.db import models
from users.models import User

class Complaint(models.Model):

    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(upload_to='complaints/', null=True, blank=True)

    location = models.CharField(max_length=255)

    latitude = models.FloatField(null=True, blank=True)

    longitude = models.FloatField(null=True, blank=True)

    category = models.CharField(max_length=100, blank=True)

    department = models.CharField(max_length=100, blank=True)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='submitted'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title