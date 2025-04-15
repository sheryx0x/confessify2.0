from django.db import models
from django.utils import timezone


class Confession(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)