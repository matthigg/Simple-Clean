"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SIMPLECLEAN_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('SIMPLECLEAN_DEBUG') == '1'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {

  # Sqlite
  # 'default': {
  #   'ENGINE': 'django.db.backends.sqlite3',
  #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  # }

  # Postgres
  'default': {
    'ENGINE':   'django.db.backends.postgresql',
    'NAME':     os.environ['SIMPLECLEAN_DATABASE_NAME'],
    'USER':     os.environ['SIMPLECLEAN_DATABASE_USER'],
    'PASSWORD': os.environ['SIMPLECLEAN_DATABASE_PASSWORD'],
    'HOST':     os.environ['SIMPLECLEAN_DATABASE_HOST'],
    'PORT':     os.environ['SIMPLECLEAN_DATABASE_PORT'],
  }
  
}

# if 'RDS_HOSTNAME' in os.environ:
#   DATABASES = {
#     'default': {
#       'ENGINE': 'django.db.backends.postgres',
#       'NAME': os.environ['RDS_DB_NAME'],
#       'USER': os.environ['RDS_USERNAME'],
#       'PASSWORD': os.environ['RDS_PASSWORD'],
#       'HOST': os.environ['RDS_HOSTNAME'],
#       'PORT': os.environ['RDS_PORT'],
#     }
#   }

# Email
EMAIL_HOST = os.environ['SES_SERVER_NAME']
EMAIL_PORT = os.environ['SES_PORT']
EMAIL_HOST_USER = os.environ['SES_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SES_PASSWORD']
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Website URL that points to the STATIC_ROOT in production
STATIC_URL = '/static/'

# This is where 'python3 manage.py collectstatic' dumps stuff
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Django will search any folders listed here for static files when developing
# locally on your own computer
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'local_static'),
  os.path.join(BASE_DIR, 'contact/static/contact'),
]