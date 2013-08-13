import datetime

from django.conf.urls import patterns, include, url
from django.utils.timezone import now

from .views import Calendar, EventCreate, EventDetail, EventUpdate, EventDelete


event_urlpatterns = patterns(
    '',
    url(r'^create/$', EventCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', EventUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', EventDelete.as_view(), name='delete'))


urlpatterns = patterns(
    '',
    # Calendar
    url(r'^$', Calendar.as_view(),
        {'year': str(now().year), 'month': str(now().month)},  # TODO: Use users local time instead of UTC
        name='calendar_default'),
    url(r'^(?P<year>\d+)-(?P<month>\d+)/$', Calendar.as_view(), name='calendar'),

    # Event
    url(r'^event/', include(event_urlpatterns, namespace='Event')))
