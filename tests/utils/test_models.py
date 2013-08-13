from django.test import TestCase

from tests.models import TestModelA, TestModelB


class TestGetAbsoluteUrlMixin(TestCase):
    urls = 'tests.urls'

    def test_reverse_via_pk(self):
        test_object = TestModelA.objects.create()
        self.assertEqual(test_object.get_absolute_url(), '/test_model/test_model_a/ahquee1daiQuo7wei0le/1/')
        self.assertEqual(test_object.get_absolute_url(url_name='update'), '/test_model/test_model_a/lahQuo2pheeM0iech7ku/1/')

    def test_reverse_via_slug(self):
        test_object = TestModelB.objects.create(slug='kel7EiMaek2thahf8aoy')
        self.assertEqual(test_object.get_absolute_url(), '/test_model/test_model_b/Udaicae3EiKai8eiveif/kel7EiMaek2thahf8aoy/')
        self.assertEqual(test_object.get_absolute_url(url_name='update'), '/test_model/test_model_b/xoorumi8Thei5ayei5io/kel7EiMaek2thahf8aoy/')
