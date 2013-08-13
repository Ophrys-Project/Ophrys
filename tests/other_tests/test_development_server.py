from django.test import TestCase
from django.test.client import Client


class DevServerTest(TestCase):
    def test_get_home_url(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
