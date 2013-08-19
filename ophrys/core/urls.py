from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import ConfigView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^config/$', ConfigView.as_view(), name='config'))
