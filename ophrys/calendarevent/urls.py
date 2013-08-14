import datetime

from django.conf.urls import patterns, include, url
from django.utils.timezone import now

from .models import Event
from .views import Calendar


urlpatterns = patterns(
    '',
    # Calendar
    url(r'^$', Calendar.as_view(),
        {'year': str(now().year), 'month': str(now().month)},  # TODO: Use users local time instead of UTC
        name='calendar_default'),
    url(r'^(?P<year>\d+)-(?P<month>\d+)/$', Calendar.as_view(), name='calendar'),

    # Event
    url(r'^event/', include(Event().urls)))
