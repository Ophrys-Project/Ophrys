from django.conf.urls import patterns, include, url


test_model_a_urlpatterns = patterns(
    '',
    url(r'^ahquee1daiQuo7wei0le/(?P<pk>\d+)/', 'some_view', name='detail'),
    url(r'^lahQuo2pheeM0iech7ku/(?P<pk>\d+)/', 'some_view', name='update'))


test_model_b_urlpatterns = patterns(
    '',
    url(r'^Udaicae3EiKai8eiveif/(?P<slug>\w+)/', 'some_view', name='detail'),
    url(r'^xoorumi8Thei5ayei5io/(?P<slug>\w+)/', 'some_view', name='update'))


test_model_urlpatterns = patterns(
    '',
    url(r'^test_model_a/', include(test_model_a_urlpatterns, namespace='TestModelA')),
    url(r'^test_model_b/', include(test_model_b_urlpatterns, namespace='TestModelB')))


urlpatterns = patterns(
    '',
    url(r'^test_model/', include(test_model_urlpatterns, namespace='tests')))
