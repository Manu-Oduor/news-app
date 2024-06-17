from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    # null is database-related, the database stores that value as NULL
    # blank is validation-related, a form allows an empty value
    age = models.PositiveIntegerField(null=True, blank=True)
