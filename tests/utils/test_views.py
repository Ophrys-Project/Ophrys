from django.template import TemplateDoesNotExist
from django.test import TestCase
from django.test.client import Client

from tests.models import TestModelC


class AutoModelMixinViewsTest(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        self.assertRaisesMessage(TemplateDoesNotExist, 'tests/testmodelc_list.html', self.client.get, '/test_model/test_model_c/')

    def test_create_view(self):
        self.assertRaisesMessage(TemplateDoesNotExist, 'tests/testmodelc_form.html', self.client.get, '/test_model/test_model_c/create/')
        response = self.client.post('/test_model/test_model_c/create/', {'name': 'aar7iNgou2viw4ahv2ve'})
        self.assertEqual(response.url, 'http://testserver/test_model/test_model_c/1/')
        self.assertTrue(TestModelC.objects.filter(name='aar7iNgou2viw4ahv2ve').exists())

    def test_detail_view(self):
        TestModelC.objects.create(name='AiwaiB5oheez1UJajeip')
        self.assertRaisesMessage(TemplateDoesNotExist, 'tests/testmodelc_detail.html', self.client.get, '/test_model/test_model_c/1/')

    def test_update_view(self):
        TestModelC.objects.create(name='Luph3tohquoesai2haLa')
        self.assertRaisesMessage(TemplateDoesNotExist, 'tests/testmodelc_form.html', self.client.get, '/test_model/test_model_c/1/update/')
        response = self.client.post('/test_model/test_model_c/1/update/', {'name': 'apeej7eiGhab3eipheem'})
        self.assertEqual(response.url, 'http://testserver/test_model/test_model_c/1/')
        self.assertFalse(TestModelC.objects.filter(name='Luph3tohquoesai2haLa').exists())
        self.assertTrue(TestModelC.objects.filter(name='apeej7eiGhab3eipheem').exists())

    def test_delete_view(self):
        TestModelC.objects.create(name='Zah6ceiGiu0ahf7ouH4h')
        self.assertTrue(TestModelC.objects.filter(name='Zah6ceiGiu0ahf7ouH4h').exists())
        self.assertRaisesMessage(TemplateDoesNotExist, 'tests/testmodelc_confirm_delete.html', self.client.get, '/test_model/test_model_c/1/delete/')
        response = self.client.post('/test_model/test_model_c/1/delete/', {})
        self.assertEqual(response.url, 'http://testserver/test_model/test_model_c/')
        self.assertFalse(TestModelC.objects.filter(name='Zah6ceiGiu0ahf7ouH4h').exists())
