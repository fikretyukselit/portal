from django.db import models


class University(models.Model):
    name = models.CharField(max_length=64, blank=False)
    city = models.CharField(max_length=24, blank=False)
    country = models.CharField(max_length=24, blank=False)
