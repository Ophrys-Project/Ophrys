from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^calendar/', include('ophrys.calendarevent.urls')),
)
