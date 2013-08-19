from django.dispatch import receiver

from ophrys.core.config import ConfigGroup, ConfigVariable
from ophrys.core.signals import get_config_groups


@receiver(get_config_groups, dispatch_uid='config_group_test_one')
def config_group_test_one(sender, **kwargs):
    return ConfigGroup(
        variables=(ConfigVariable(key='config_var_eexooc5goh0eiCheeth0',
                                  value='faithoh2ooTh5eighooT',
                                  label='Label for config_var_eexooc5goh0eiCheeth0'),
                   ConfigVariable(key='config_var_ooy4Ra2daezaequ4phai', value=42),
                   ConfigVariable(key='config_var_no3rohchitie6Caebaew', value=True)),
        title='Title for config_group_test_one_veey2mohfoogooh7Wio4')
