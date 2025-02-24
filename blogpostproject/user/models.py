from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    imageURL = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    
