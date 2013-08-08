from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^ahquee1daiQuo7wei0le/(?P<pk>\d+)/', 'django.contrib.auth.views.login', name='tests.models.TestModelA.detail'),
    url(r'^lahQuo2pheeM0iech7ku/(?P<pk>\d+)/', 'django.contrib.auth.views.login', name='tests.models.TestModelA.update'),
    url(r'^Udaicae3EiKai8eiveif/(?P<slug>\w+)/', 'django.contrib.auth.views.login', name='tests.models.TestModelB.detail'),
    url(r'^xoorumi8Thei5ayei5io/(?P<slug>\w+)/', 'django.contrib.auth.views.login', name='tests.models.TestModelB.update'),
)
