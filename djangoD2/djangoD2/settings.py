"""
Django settings for djangoD2 project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7zfcz4za_@yf4*=6z=goxv5i7y&%(hf6-7#pt0i*a@@iq&rl!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'internet_shop',
    'news_portal.apps.NewPortalConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'django_celery_beat',
    'fpages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'debug_toolbar',
    'django_apscheduler',
]

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

ROOT_URLCONF = 'djangoD2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

WSGI_APPLICATION = 'djangoD2.wsgi.application'

ACCOUNT_FORMS = {'signup': 'account.forms.CommonSignupForm'}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'OPTIONS': {'timeout': 5, }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
#
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = os.getenv(
    'HOST_USER')  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_ADDR')

ADMINS = [
    ('yana', os.getenv('EMAIL ADMIN')),
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = 'Django07.22@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # Указываем, куда будем сохранять кэшируемые файлы!
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)-8s %(message)s',
        },
        'console_warning': {
            'format': '%(asctime)s %(pathname)s %(levelname)-8s %(message)s',
        },
        'console_error': {
            'format': '%(levelname)-8s [%(asctime)s] [%(name)s:%(module)s:%(funcName)s:%(lineno)s] [%(exc_info)s] %('
                      'message)s',
        },
        'file_info': {
            'format': '	%(levelno)s [%(asctime)s] [%(name)s:%(module)s] %(''message)s',
        },
        'file_error': {
            'format': '%(asctime)s %(levelname)-8s %(pathname)s %(exc_info)s  %(''message)s',
        },
        'file_security': {
            'format': '%(levelname)-8s [%(asctime)s] [%(name)s:%(module)s %(''message)s',
        },
        'mail': {
            'format': '%(asctime)s %(levelname)-8s %(pathname)s  %(''message)s',
        },

    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',

        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error'
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file_info',
            'filters': ['require_debug_false'],
            'filename': 'general.log'
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'file_error',
            'filename': 'errors.log'
        },
        'file_security': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'file_security',
            'filename': 'security.log'
        },

        'mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail',
            'filters': ['require_debug_false'],
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_info'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_error', 'mail'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_error', 'mail'],
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_error'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_error'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': False,
        },
    }
}
