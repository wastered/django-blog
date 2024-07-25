from server.settings.components import config
from server.settings.components.common import (
    INSTALLED_APPS, DATABASES,

)

DEBUG = True

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    'localhost',
    '0.0.0.0',  # noqa: S104
    '127.0.0.1',
    '[::1]',
]

# Disable persistent DB connections
# https://docs.djangoproject.com/en/4.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0

# Installed apps for development only:

INSTALLED_APPS += (
    # Linting migrations:
    # https://github.com/3YOURMIND/django-migration-linter
    'django_migration_linter',
)

