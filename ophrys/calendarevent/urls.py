from django.conf.urls import patterns, include, url

from .views import EventDetail


urlpatterns = patterns(
    '',
    url(r'^event/(?P<pk>\d+)/$', EventDetail.as_view(), name='ophrys.calendarevent.models.Event.detail'),
)
