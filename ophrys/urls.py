from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^calendar/', include('ophrys.calendarevent.urls', namespace='ophrys.calendarevent')),
    url(r'^', include('ophrys.core.urls', namespace='ophrys.core')))
