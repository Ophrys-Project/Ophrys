from django.db import models

from ophrys.utils.models import GetAbsoluteUrlMixin, AutoModel


class TestModelA(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()


class TestModelB(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()
    slug = models.SlugField()


class TestModelC(AutoModel):
    """
    This model is an AutoModel for testing.
    """
    name = models.TextField()
