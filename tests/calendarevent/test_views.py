import datetime

from django.test import TestCase
from django.test.client import Client
from django.utils.timezone import now, utc

from ophrys.calendarevent.models import Event


class TestCalendar(TestCase):
    def setUp(self):
        self.client = Client()

    def test_calendar_view_default(self):
        event_1 = Event.objects.create(title='ohP3thu9aiviepaeFeph', begin=now())
        event_2 = Event.objects.create(title='Queiv1oojuLuip9Wo0qu', begin=now()-datetime.timedelta(days=31))
        response = self.client.get('/calendar/')
        self.assertContains(response, 'ohP3thu9aiviepaeFeph')
        self.assertNotContains(response, 'Queiv1oojuLuip9Wo0qu')

    def test_calendar_view_specific(self):
        event_1 = Event.objects.create(title='Oochai4aigohheiXohpe', begin=now())
        event_2 = Event.objects.create(title='ahba2Ahzee5Ochohth8u', begin=datetime.datetime(2013, 7, 20, tzinfo=utc))
        response = self.client.get('/calendar/2013-07/')
        self.assertNotContains(response, 'Oochai4aigohheiXohpe')
        self.assertContains(response, 'ahba2Ahzee5Ochohth8u')
