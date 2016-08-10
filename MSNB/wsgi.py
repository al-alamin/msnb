"""
WSGI config for MSNB.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, site

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MSNB.settings")
# linode specific settings
# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/.virtualenvs/wcsenvpython3/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/html/mystudynotebook.com/MSNB')
sys.path.append('/var/www/html/mystudynotebook.com/MSNB/MSNB')
# Activate your virtual env
activate_env=os.path.expanduser("/home/.virtualenvs/wcsenvpython3/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()




application = get_wsgi_application()
