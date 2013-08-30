import datetime

from django.db import models
from django.utils.translation import ugettext_lazy

from ophrys.core.models import TaggedModel
from ophrys.utils.models import AutoModelMixin


class Event(AutoModelMixin, TaggedModel):
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
