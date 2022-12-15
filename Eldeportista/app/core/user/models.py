from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ci = models.CharField(max_length=150, verbose_name='Cedula', unique=True)