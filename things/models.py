from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(AbstractUser):
    name = models.CharField(unique=True, blank=False,max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
