import os
import sys

path = '/var/www/mpp'
if path not in sys.path:
    sys.path.append(path)
path = '/var/www/mpp/mysite'
if path not in sys.path:
    sys.path[0:0]=[path]
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
