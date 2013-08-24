from django import forms
from django.dispatch import receiver
from django.utils.translation import ugettext as _

from .models import ConfigStore
from .signals import get_config_groups


class Config:
    """
    Container class for all config variables.

    The several variables are attributes of an instance of this class.
    """
    def __getattr__(self, key):
        try:
            return self._cache(key)
        except TypeError:
            # The key is not in the cache.
            pass
        try:
            return self._database(key)
        except TypeError:
            # The key is not in the database
            pass
        try:
            default_value = get_default_value(key)
        except TypeError as error_message:
            raise AttributeError(error_message)
        return default_value

    def __setattr__(self, key, value):
        updated_rows = ConfigStore.objects.filter(key=key).update(value=value)
        if not updated_rows:
            ConfigStore.objects.create(key=key, value=value)

    def _cache(self, key):
        # The cache does not exist at the moment.
        raise TypeError

    def _database(self, key):
        try:
            return ConfigStore.objects.get(key=key).value
        except ConfigStore.DoesNotExist:
            raise TypeError


config = Config()
"""
Container object. Final entry point to get an set config variables. The
serveral variables are attributes of this object.
"""


class ConfigVariable:
    """
    Simple class for a default config variable.
    """
    def __init__(self, key, value, **field_kwargs):
        self.key = key
        self.value = value
        self.field_kwargs = field_kwargs

    @property
    def form_field(self):
        """
        Returns the form field for the variable.
        """
        if isinstance(self.value, bool):
            return forms.BooleanField(required=False, **self.field_kwargs)
        elif isinstance(self.value, int):
            return forms.IntegerField(**self.field_kwargs)
        else:  # str
            return forms.CharField(**self.field_kwargs)


class ConfigGroup:
    """
    Simple class for a group of default config variables.
    """
    def __init__(self, variables, title=None):
        self.variables = variables
        self.title = title

    def __getitem__(self, key):
        for variable in self.variables:
            if key == variable.key:
                return variable
        else:
            raise KeyError

    def __iter__(self):
        for variable in self.variables:
            yield variable

    def __contains__(self, item):
        if isinstance(item, ConfigVariable):
            return item in self.variables
        else:
            for variable in self.variables:
                if variable.key == item:
                    return True
            else:
                return False


def get_default_value(key):
    """
    Function to get the default value of a variable.
    """
    config_groups_list = get_config_groups.send(sender='get_default_value_function')
    for receiver, config_group in config_groups_list:
        try:
            value = config_group[key].value
        except KeyError:
            continue
        else:
            return value
    else:
        raise TypeError('Config variable %s does not exist' % key)


def context_processor(request):
    """
    This puts the config object into every RequestContext. It has to be set in
    the TEMPLATE_CONTEXT_PROCESSORS setting.
    """
    return {'config': config}


@receiver(get_config_groups, dispatch_uid='general_config_variables')
def general_config_variables(sender, **kwargs):
    return ConfigGroup(
        variables=(ConfigVariable(key='organisation_name',
                                  value='Name of your Organisation',
                                  label='Name of the Organisation'),),
        title=_('General settings'))
