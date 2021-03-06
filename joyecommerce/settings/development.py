from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

# INSTALLED_APPS += [
#      'debug_toolbar',
# ]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USERNAME'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE_KEY = 'pk_test_G4TyVipBeThWHPRCzhHlgduO00yNMNAv2R'
# STRIPE_PUBLIC_KEY=''
# STRIPE_SECRET_KEY=''
STRIPE_SECRET_KEY = 'sk_test_lsI9uVZY8xnYapjhMUZVTRGM002HRsW1De'