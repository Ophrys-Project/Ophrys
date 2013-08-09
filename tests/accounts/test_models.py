from django.test import TestCase

from ophrys.accounts.models import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='weefoo3uy0joop7Thaiy@example.com')

    def test_str(self):
        self.assertEqual(str(self.user), 'weefoo3uy0joop7Thaiy@example.com')

    def test_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Full name: weefoo3uy0joop7Thaiy@example.com')

    def test_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Short name: weefoo3uy0joop7Thaiy@example.com')

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email='Yie4nish9joThuw2Ohla@example.com', password='default')
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_without_email(self):
        self.assertRaisesMessage(ValueError, 'The given email must be set.', User.objects.create_superuser, email='', password='default')
