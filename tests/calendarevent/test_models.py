import datetime

from django.test import TestCase

from ophrys.calendarevent.models import Tag, Event


class TestTag(TestCase):
    def test_str(self):
        Tag.objects.create(name='ohput4chahFaeGh7ieng')
        self.assertEqual(str(Tag.objects.get(pk=1)), 'ohput4chahFaeGh7ieng')


class TestEvent(TestCase):
    def setUp(self):
        self.event = Event.objects.create(title='kohp3hah9Bei2eo3aije', begin=datetime.datetime.now(datetime.timezone.utc))

    def test_str(self):
        self.assertEqual(str(self.event), 'kohp3hah9Bei2eo3aije')

    def test_end(self):
        self.assertTrue(self.event.end is None)
        event_2 = Event.objects.create(title='quai3Aeshahthagheiru',
                                       begin=datetime.datetime(2013, 7, 20, 13, 30, tzinfo=datetime.timezone.utc),
                                       duration=45)
        self.assertEqual(event_2.end, datetime.datetime(2013, 7, 20, 14, 15, tzinfo=datetime.timezone.utc))
