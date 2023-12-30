from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # we redefine the email field:
    email = models.EmailField(unique=True)