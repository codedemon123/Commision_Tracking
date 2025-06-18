from django.db import models
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admissions', 'Admissions'),
        ('Accounts', 'Accounts'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.user.username