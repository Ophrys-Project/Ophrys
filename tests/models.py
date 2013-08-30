from django.db import models

from ophrys.core.models import TaggedModel
from ophrys.utils.models import GetAbsoluteUrlMixin, AutoModelMixin


class TestModelA(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()


class TestModelB(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()
    slug = models.SlugField()


class TestModelC(AutoModelMixin, models.Model):
    """
    This model is mixed with AutoModelMixin for testing.
    """
    name = models.TextField()


class TestModelD(TaggedModel):
    """
    This model is a tagged model for testing.
    """
    name = models.TextField()


from .config import config_group_test_one
"""
Imports the test config variables to connect the relevant signal.
"""
