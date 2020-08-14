"""
Django settings for dmonitor project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&y)w9q)as=kno)0wwfbaz%l1=orqsmpt4jmnuj7#6+77az6%!k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 生产环境应该改为False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    # 添加django-xadmin

    'django_celery_beat',
    # django-celery-beat

    'django_celery_results',
    # django-celery-results

    'rest_framework',
    # django-rest-framework

    'import_export',
    # django-import-export

    'drf_yasg',
    # drf-yasg

    'silk',
    # django-silk

    'debug_toolbar',
    # django-debug-toolbar
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'dmonitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'dmonitor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmonitor',
        'HOST': '192.168.1.101',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'Abcdef@123456',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}
# MySQL数据库配置

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
# 简体中文界面

TIME_ZONE = 'Asia/Shanghai'
# 亚洲/上海时区

USE_I18N = True

USE_L10N = True

USE_TZ = False
# 不使用国际标准时间

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 定义静态文件的目录

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 定义媒体文件存放的目录


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'default': {
            'level': 'INFO',
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s',
            'encoding': 'utf-8',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
# 日志配置


CELERY_ENABLE_UTC = False
# 不使用国际标准时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 使用亚洲/上海时区
DJANGO_CELERY_BEAT_TZ_AWARE = False
# 解决时区问题
CELERY_BROKER_URL = 'redis://localhost:6379/0'
# redis://:password@hostname:port/db_number
CELERY_BROKER_TRANSPORT = 'redis'
# 使用redis作为中间件
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# 自定义调度类，使用Django的ORM
CELERY_RESULT_BACKEND = 'django-db'
# 任务结果，使用Django的ORM
CELERY_ACCEPT_CONTENT = ['application/json']
# 设置任务接收的序列化类型
CELERY_TASK_SERIALIZER = 'json'
# 设置任务序列化方式
CELERY_RESULT_SERIALIZER = 'json'
# 设置结果序列化方式


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.xxx.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'yyy@www.zzz.com'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'ccc@www.ddd.com'
# SMTP服务配置


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "IGNORE_EXCEPTIONS": True,
        }
    }
}
# django-redis配置


IMPORT_EXPORT_USE_TRANSACTIONS = True
# 在导入数据时使用数据库事务，默认False


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
# django-rest-framework配置


MONITOR_PLATFORM = "http://www.monitor.com/admin/"
# 生产环境接口监控平台地址


INTERNAL_IPS = [
    '127.0.0.1',
]
# django-debug-toolbar配置
