from django.db import models

from ophrys.utils.models import GetAbsoluteUrlMixin


class TestModelA(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()


class TestModelB(GetAbsoluteUrlMixin, models.Model):
    name = models.TextField()
    slug = models.SlugField()
