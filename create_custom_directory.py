# -*- coding: utf-8 -*-

import base64
import os


SETTINGS_CONTENT = """# -*- coding: utf-8 -*-
#
# Custom settings for ophrys project.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/dev/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/dev/ref/settings/

from ophrys.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = %(secret_key)r

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

WSGI_APPLICATION = 'ophrys_custom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3'),
    }
}
"""


WSGI_CONTENT = r"""# -*- coding: utf-8 -*-
#
# WSGI config for ophrys project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ophrys_custom.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""


def main():
    """
    Main entry of the script.
    """
    directory_path = create_directory()
    create_init(directory_path=directory_path)
    create_settings(directory_path=directory_path)
    create_wsgi_file(directory_path=directory_path)


def create_directory():
    """
    Creates the directory for the custom files.
    """
    directory_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'ophrys_custom')
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
        print('Directory %s successfully created.' % directory_path)
    return directory_path


def create_init(directory_path):
    """
    Creates an empty __init__.py file in the custom directory.
    """
    init_file_path = os.path.join(directory_path, '__init__.py')
    if not os.path.exists(init_file_path):
        open(init_file_path, 'w').close()
        print('File %s successfully created.' % init_file_path)


def create_settings(directory_path):
    """
    Creates the settings.py file in the custom directory.
    """
    settings_file_path = os.path.join(directory_path, 'settings.py')
    if not os.path.exists(settings_file_path):
        with open(settings_file_path, 'w') as settings_file:
            settings_file.write(SETTINGS_CONTENT % {'secret_key': base64.b64encode(os.urandom(30)).decode()})
        print('Settings file %s successfully created.' % settings_file_path)
    else:
        print('Settings file %s already exists.' % settings_file_path)


def create_wsgi_file(directory_path):
    """
    Creates the wsgi.py file in the custom directory.
    """
    wsgi_file_path = os.path.join(directory_path, 'wsgi.py')
    if not os.path.exists(wsgi_file_path):
        with open(wsgi_file_path, 'w') as wsgi_file:
            wsgi_file.write(WSGI_CONTENT)
        print('File %s successfully created.' % wsgi_file_path)
    else:
        print('File %s already exists.' % wsgi_file_path)


if __name__ == '__main__':
    main()
