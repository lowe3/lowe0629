"""
Django settings for LinebotFunc project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import psycopg2

# conn = psycopg2.connect(
# database = "d4jgiqvfjf2nde",
# user = "rdvsrzpesjtzad",
# password = "eddaf28d42616aba0fd4de92aeb8df4d1e33c6e1ae6a202da17fd1d6cd39fbaf",
# host = "ec2-34-200-101-236.compute-1.amazonaws.com",
# port = "5432")

# cur = conn.cursor()
# cur.execute("CREATE TABLE USER(
# ID          VARCHAR(50) PRIMARY KEY   NOT NULL,
# HEIGHT      INT                       NOT NULL,
# WEIGHT      INT                       NOT NULL,
# AGE         INT                       NOT NULL,
# GENDER      VARCHAR(10)               NOT NULL,
# BMR         INT                       NOT NULL);")

# conn.commit()
# conn.close()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&l-5u1cp_63ks5@g$-^j&3^&czbaw9hb9ymz)1+^9j2)cbdp)8'
LINE_CHANNEL_ACCESS_TOKEN = 'oYe2K3pCaFvBRfJXeh/gVeQntwTeHUkCz17OCjPL/3T54t9pzeqDaz0wpeZBQKNgxT4MZylIJZjLEroLFbCWHeCqdvDsLBUAFrpa6KDkLO1oSpHewvjZsTfCNilpTGiWCKOfk6ds72by1J0GRdpBIAdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECERT = 'c764ddee54ead77137b855602e6257fb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'funclapi',
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

ROOT_URLCONF = 'LinebotFunc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'LinebotFunc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
      os.path.join(BASE_DIR,'static'),]
	  
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600,ssl_require=True)