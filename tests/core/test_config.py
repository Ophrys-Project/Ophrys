from django.test import TestCase
from django.test.client import Client

from ophrys.core.config import config, ConfigVariable
from ophrys.core.models import ConfigStore
from ophrys.core.signals import get_config_groups


class ConfigTest(TestCase):
    def test_get_config_var_default_value(self):
        self.assertEqual(config.config_var_eexooc5goh0eiCheeth0, 'faithoh2ooTh5eighooT')

    def test_get_config_var_from_database(self):
        ConfigStore.objects.create(key='config_var_johTho7uovikie6to8so', value='sahGaomoozoesheeQu2e')
        with self.assertNumQueries(1):
            self.assertEqual(config.config_var_johTho7uovikie6to8so, 'sahGaomoozoesheeQu2e')

    def test_get_not_existing_config_var(self):
        def get_var(key):
            return getattr(config, key)
        self.assertRaisesMessage(
            AttributeError,
            'Config variable not_existing_variable_geitheyieYeisheJai5k does not exist',
            get_var,
            'not_existing_variable_geitheyieYeisheJai5k')

    def test_set_config_var_with_get_default_before(self):
        self.assertEqual(config.config_var_eexooc5goh0eiCheeth0, 'faithoh2ooTh5eighooT')
        with self.assertNumQueries(2):
            config.config_var_eexooc5goh0eiCheeth0 = 'AiwusheFoo1moht7weng'
        self.assertEqual(config.config_var_eexooc5goh0eiCheeth0, 'AiwusheFoo1moht7weng')

    def test_set_config_var_without_get_default_before(self):
        with self.assertNumQueries(2):
            config.config_var_faithoh2ooTh5eighooT = 'azoo4Tu7ea4Nan7eiphe'
        self.assertEqual(config.config_var_faithoh2ooTh5eighooT, 'azoo4Tu7ea4Nan7eiphe')

    def test_set_config_var_which_exists_in_database_before(self):
        ConfigStore.objects.create(key='config_var_er1chaWapheoTe1iecei', value='aB9ahphuthiekohqu7ub')
        with self.assertNumQueries(1):
            config.config_var_er1chaWapheoTe1iecei = 'gahmahniethohgh0AiRo'
        self.assertEqual(config.config_var_er1chaWapheoTe1iecei, 'gahmahniethohgh0AiRo')

    def get_config_group_test_one(self):
        """
        Helper function for some tests.
        """
        for receiver, config_group in get_config_groups.send(sender=self):
            if 'Title for config_group_test_one_veey2mohfoogooh7Wio4' == config_group.title:
                return config_group

    def test_config_group_contains_variables_via_key(self):
        config_group = self.get_config_group_test_one()
        self.assertTrue('config_var_eexooc5goh0eiCheeth0' in config_group)
        self.assertFalse('not_existing_variable_geitheyieYeisheJai5k' in config_group)

    def test_config_group_contains_variables_via_variable(self):
        config_group = self.get_config_group_test_one()
        config_variable = config_group['config_var_eexooc5goh0eiCheeth0']
        self.assertTrue(config_variable in config_group)
        self.assertFalse(ConfigVariable(key='some_key_vaagoopaego7eik3au1T', value=45213574512) in config_group)


class ConfigViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get('/config/')
        self.assertTemplateUsed(response, 'core/config_form.html')
        self.assertContains(response, 'config_var_eexooc5goh0eiCheeth0')
        self.assertContains(response, 'faithoh2ooTh5eighooT')
        self.assertContains(response, 'Label for config_var_eexooc5goh0eiCheeth0')
        self.assertContains(response, 'Title for config_group_test_one_veey2mohfoogooh7Wio4')

    def test_post(self):
        post_data = self.client.get('/config/').context['form'].initial
        num_queries = len(post_data)*3
        post_data['config_var_eexooc5goh0eiCheeth0'] = 'OoSoxoh2Ees1Quiz9roh'
        post_data['config_var_ooy4Ra2daezaequ4phai'] = 122
        post_data.pop('config_var_no3rohchitie6Caebaew')
        with self.assertNumQueries(num_queries):  # 3 queries per variable
            response = self.client.post('/config/', post_data)
            self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/config/')
        self.assertEqual(config.config_var_eexooc5goh0eiCheeth0, 'OoSoxoh2Ees1Quiz9roh')
        self.assertEqual(config.config_var_ooy4Ra2daezaequ4phai, 122)
        self.assertFalse(config.config_var_no3rohchitie6Caebaew)


class ConfigVariablesTest(TestCase):
    def test_organisation_name(self):
        self.assertEqual(config.organisation_name, 'Name of your Organisation')

    def test_appearance(self):
        config.organisation_name = 'ahr7ais0beuph6Iev2Wo'
        response = Client().get('/')
        self.assertContains(response, '<title>ahr7ais0beuph6Iev2Wo</title>')
