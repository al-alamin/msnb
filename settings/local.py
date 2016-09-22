from .base import *

DEBUG = True
# DEBUG_PROPAGATE_EXCEPTIONS = True
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

# logging settings for local. print to console. in production save to file
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, '../media/')
MEDIA_URL = 'media/'

ADMIN_EMAILS = [ 'mdabdullahalalaminp@gmail.com', ]
PRIMARY_ADMIN_EMAIL = 'mdabdullahalalaminp@gmail.com'
ADMINS = [('Alamin', 'mdabdullahalalaminp@gmail.com')]
