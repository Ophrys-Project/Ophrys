from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy

from jsonfield import JSONField


class ConfigStore(models.Model):
    """
    Model to store customized config variables in the database.
    """
    key = models.CharField(max_length=255)
    value = JSONField()


class Tag(models.Model):
    """
    Model for tags.
    """
    name = models.CharField(max_length=255, help_text=ugettext_lazy('Maximum 255 characters'))
    """
    Name of the tag, a string up to 255 characters.
    """

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name.isalnum():
            raise TypeError("A tag's name should contain only alphanumeric characters.")
        return super().save(*args, **kwargs)


class TagConnection(models.Model):
    """
    Intern connection model to connect a tag to a tagged item.
    """
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    class Meta:
        ordering = ('tag',)


class TaggedModel(models.Model):
    """
    Abstract model class for taggable models.
    """
    tag_connections = generic.GenericRelation(TagConnection)

    class Meta:
        abstract = True

    def get_tags(self):
        """
        Generator method to get all tags this model instance is tagged with.
        """
        for tag_connection in self.tag_connections.select_related('tag').all():
            yield tag_connection.tag

    def add_tag(self, tag):
        """
        Method to add a tag to an instance of this model.
        """
        if isinstance(tag, str):
            tag, created = Tag.objects.get_or_create(name=tag)
        TagConnection.objects.create(tag=tag, content_object=self)
