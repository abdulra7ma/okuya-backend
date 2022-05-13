# Django imports
from django.db import models
from django.db.models.base import Model
from django.utils import timezone


class DateTimeMixin(models.Model):
    """Abstract Date Time model"""

    date_joined = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
