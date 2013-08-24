from django.db import models

from jsonfield import JSONField


class ConfigStore(models.Model):
    """
    Model to store customized config variables in the database.
    """
    key = models.CharField(max_length=255)
    value = JSONField()
