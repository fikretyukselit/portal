from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    city = models.CharField(max_length=24, blank=False)
    country = models.CharField(max_length=24, blank=False)
    tc_id = models.CharField(
        validators=[RegexValidator(regex='^.{11}$', message='TC ID should have 11 digits', code='nomatch')],
        max_length=64, blank=True)
