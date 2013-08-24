from django.test import TestCase

from ophrys.core.models import Tag, TagConnection

from tests.models import TestModelD


class TaggedModelTest(TestCase):
    def setUp(self):
        self.tag_1 = Tag.objects.create(name='yegahhahraing9Udoh7c')
        self.tag_2 = Tag.objects.create(name='iei6rair0Beeviu4ieG2')
        self.object_1 = TestModelD.objects.create(name='vethah2ozah3Ael7quue')

    def test_tag_str(self):
        self.assertEqual(str(self.tag_1), 'yegahhahraing9Udoh7c')

    def test_get_tags(self):
        TagConnection.objects.create(tag=self.tag_1, content_object=self.object_1)
        TagConnection.objects.create(tag=self.tag_2, content_object=self.object_1)
        with self.assertNumQueries(1):
            self.assertEqual(list(self.object_1.get_tags()), [self.tag_2, self.tag_1])

    def test_add_tag_via_object(self):
        with self.assertNumQueries(1):
            self.object_1.add_tag(self.tag_1)
        with self.assertNumQueries(1):
            self.assertEqual(list(self.object_1.get_tags()), [self.tag_1])

    def test_add_tag_via_string(self):
        with self.assertNumQueries(2):
            self.object_1.add_tag('yegahhahraing9Udoh7c')
        with self.assertNumQueries(1):
            self.assertEqual(list(self.object_1.get_tags()), [self.tag_1])

    def test_add_new_tag_via_string(self):
        with self.assertNumQueries(6):  # TODO: Why so much? Check for performance improvements.
            self.object_1.add_tag('kahLaek1em3kie2ier6n')
        with self.assertNumQueries(1):
            self.assertEqual(list(self.object_1.get_tags())[0].name, 'kahLaek1em3kie2ier6n')
        self.assertTrue(Tag.objects.filter(name='kahLaek1em3kie2ier6n').exists())

    def test_add_new_tag_via_bad_string(self):
        self.assertRaisesMessage(TypeError, "A tag's name should contain only alphanumeric characters.", self.object_1.add_tag, 'BadString%%&&//')
