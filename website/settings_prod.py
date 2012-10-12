# Django settings for main project in prod mode

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'swept_server_v1',
    'USER': 'admin',
    'PASSWORD': 'puWwutQanJXFcb4w',
    'HOST': '',
    'PORT': '',
  }
}

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/sites/swept.in/static/'

DEFAULT_FROM_EMAIL = 'Swept <website@swept.in>'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = 'website@swept.in'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'swept'
EMAIL_HOST_PASSWORD = '16389bc9-572a-4b81-8ce9-b814247a7508'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'website.wsgi.application'