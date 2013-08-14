from django.conf.urls import patterns, include, url

from tests.models import TestModelC


test_model_a_urlpatterns = patterns(
    '',
    url(r'^ohl9pheengooLai0noo1/', 'some_view', name='list'),
    url(r'^ahquee1daiQuo7wei0le/(?P<pk>\d+)/', 'some_view', name='detail'),
    url(r'^lahQuo2pheeM0iech7ku/(?P<pk>\d+)/', 'some_view', name='update'))


test_model_b_urlpatterns = patterns(
    '',
    url(r'^Udaicae3EiKai8eiveif/(?P<slug>\w+)/', 'some_view', name='detail'),
    url(r'^xoorumi8Thei5ayei5io/(?P<slug>\w+)/', 'some_view', name='update'))


test_model_urlpatterns = patterns(
    '',
    url(r'^test_model_a/', include(test_model_a_urlpatterns, namespace='TestModelA')),
    url(r'^test_model_b/', include(test_model_b_urlpatterns, namespace='TestModelB')),
    url(r'^test_model_c/', include(TestModelC().urls)))


urlpatterns = patterns(
    '',
    url(r'^test_model/', include(test_model_urlpatterns, namespace='tests')))
