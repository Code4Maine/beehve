"""
Django settings for our beehve project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

from configurations import Configuration, values


class Common(Configuration):

    ADMINS = (
        ('Admin', 'info@example.com'),
    )

    MANAGERS = ADMINS

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, 'beehve/apps'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = []

    AUTH_PROFILE_MODULE = 'workers.Worker'

    # Application definition

    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.google',
        'django_extensions',
        'floppyforms',
        'avatar',
        'markdown_deux',
        'djangobower',
        'bootstrap3',
        'djcelery',

        'homepage',
        'honey',
        'workers',
    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, "beehve/templates") ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                    # list if you haven't customized them:
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'honey.context_processors.menu_preloader',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        'djangobower.finders.BowerFinder',
    )

    BOWER_COMPONENTS_ROOT= os.path.join(BASE_DIR, 'components')

    BOWER_INSTALLED_APPS = (
        'jquery#2.1.1',
        'bootstrap#3.2.0',
        'font-awesome#4.1.0',
        'morrisjs#0.5.1',
        'timeline#2.29.1', 
        'raphael#2.1.2',
        'bootstrap-multiselect#0.9.5',
        'bootstrap-colorpicker',
        'underscore',
        'isotope',
    )


    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "workers.backends.EmailOrUsernameModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",)

    ROOT_URLCONF = 'beehve.urls'

    WSGI_APPLICATION = 'beehve.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3'),
        environ=True))

    BROKER_URL = values.Value('redis://localhost:6379/0')
    CELERY_RESULT_BACKEND=values.Value('djcelery.backends.database:DatabaseBackend')
    CELERY_TIMEZONE = values.Value('UTC')
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

    from datetime import timedelta

    CELERYBEAT_SCHEDULE = {
        'check-git-repos': {
            'task': 'honey.tasks.check_git_repos',
            'schedule': timedelta(seconds=60),
            'args': ()
        },
    }

    NEVERCACHE_KEY = values.Value('klladsf-wefkjlwef-wekjlwef--wefjlkjfslkxvl')

    #CACHES = values.CacheURLValue('memcached://127.0.0.1:11211')

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/New_York'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

    PUBLIC_ROOT = values.Value(os.path.join(BASE_DIR, 'public'))
    STATIC_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'media')
    MEDIA_URL = "/media/"

    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = values.Value('beehve-media')

    AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
                   'Cache-Control': 'max-age=86400', }

    if AWS_ACCESS_KEY_ID.setup('AWS_ACCESS_KEY_ID'):
        MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
        DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "beehve/static"),
    )

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 14

    LOGIN_EXEMPT_URLS = ['', '/',
                         '/accounts/login/',
                         'login',
                         '/accounts/signup/']

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_URL = '/accounts/logout/'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    SECRET_KEY = 'notasecretatall'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    HONEY_COMMITS_SINCE_DAYS = 260 

    #INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)

    #MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + (
    #    'debug_toolbar.middleware.DebugToolbarMiddleware',)


class Stage(Common):
    DEBUG = True

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value('localhost')
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(False)


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = False

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(True)

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    if DSN_VALUE:
        RAVEN_CONFIG = {
            'dsn': DSN_VALUE.setup('DSN_VALUE'),
        }

        INSTALLED_APPS = Common.INSTALLED_APPS + (
            'raven.contrib.django.raven_compat',)
