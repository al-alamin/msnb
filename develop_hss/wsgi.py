"""
WSGI config for HSS_Obaida project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, site

from django.core.wsgi import get_wsgi_application
# Add the site-packages of the chosen virtualenv to work with
# site.addsitedir('/var/www/html/whitecanvassoft.com/wcsenv/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
# sys.path.append('/var/www/html/DEVELOP.HSS/develop_hss')
# sys.path.append('/var/www/html/DEVELOP.HSS/develop_hss/develop_hss')
# Activate your virtual env
# activate_env=os.path.expanduser("/var/www/html/whitecanvassoft.com/wcsenv/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "develop_hss.settings")


application = get_wsgi_application()
