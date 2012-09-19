# Django settings for main project in dev mode

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'swept_local',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }
}


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'