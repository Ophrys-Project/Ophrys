import datetime

from django.db import models
from django.utils.translation import ugettext_lazy

from ophrys.utils.models import GetAbsoluteUrlMixin, AutoModel


class Tag(models.Model):
    """
    Model for event tags.
    """
    name = models.CharField(max_length=255, help_text=ugettext_lazy('Maximum 255 characters'))
    """
    Name of the event tag, a string up to 255 characters.
    """

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Event(AutoModel):
    """
    Model for an event in the community.
    """
    title = models.CharField(max_length=255, help_text=ugettext_lazy('Maximum 255 characters'))
    """
    Title of the event, a string up to 255 characters.
    """

    text = models.TextField(blank=True)
    """
    Description of the event. This field is optional.
    """

    begin = models.DateTimeField()
    """
    Begin of the event. You can set date and time.
    """

    duration = models.IntegerField(null=True, blank=True, help_text=ugettext_lazy('Duration of the event in minutes'))
    """
    Duration of the event in minutes.
    """

    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='events')
    """
    One or more tags related to the event. The tags are instances of the Tag model.
    """

    class Meta:
        ordering = ('begin',)

    def __str__(self):
        return self.title

    @property
    def end(self):
        """
        Returns the end time of the event according to begin and duration.
        """
        if self.duration:
            return self.begin + datetime.timedelta(minutes=self.duration)
