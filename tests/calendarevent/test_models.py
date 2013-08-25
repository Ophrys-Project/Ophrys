import datetime

from django.test import TestCase
from django.utils.timezone import now, utc

from ophrys.calendarevent.models import Event
from ophrys.core.models import Tag


class TestTag(TestCase):
    def test_add_tag(self):
        event = Event.objects.create(title='ohput4chahFaeGh7ieng', begin=now())
        event.add_tag('oxgath4VohheeYahxeiW')
        self.assertTrue(Tag.objects.get(name='oxgath4VohheeYahxeiW') in event.get_tags())


class TestEvent(TestCase):
    def setUp(self):
        self.event = Event.objects.create(title='kohp3hah9Bei2eo3aije', begin=now())

    def test_str(self):
        self.assertEqual(str(self.event), 'kohp3hah9Bei2eo3aije')

    def test_end(self):
        self.assertTrue(self.event.end is None)
        event_2 = Event.objects.create(title='quai3Aeshahthagheiru',
                                       begin=datetime.datetime(2013, 7, 20, 13, 30, tzinfo=utc),
                                       duration=45)
        self.assertEqual(event_2.end, datetime.datetime(2013, 7, 20, 14, 15, tzinfo=utc))
