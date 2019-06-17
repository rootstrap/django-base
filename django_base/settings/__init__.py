import os
import importlib

# import base settings for all environments
from .base import *  # noqa

# import specific settings depending on the environment
ENV_ROLE = os.getenv('ENV_ROLE', 'development')
env_settings = importlib.import_module(f'django_base.settings.{ENV_ROLE}')

globals().update(vars(env_settings))

if os.getenv('DYNO'):
    # Heroku settings must be run not imported this is due to certain
    # declarations of variables.
    django_heroku.settings(locals(), test_runner=False)
    exec(open('/app/django_base/settings/heroku.py').read())

try:
    # import local settings if present
    from .local import *  # noqa
except ImportError:
    pass
