from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
