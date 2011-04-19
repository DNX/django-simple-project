import os
import sys 

os.environ['DJANGO_SETTINGS_MODULE'] = 'simple_project.settings'
sys.path.insert(0, '/home/user/projects/production')
sys.path.insert(0, '/home/user/projects/production/simple_project')

# This has to be done here otherwise Django won't be in a directory
# that's in PYTHONPATH.
from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()