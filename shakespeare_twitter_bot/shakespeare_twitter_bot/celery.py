from celery import Celery
from django.conf import settings
import os
 
# Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
 
app = Celery('myproject')
app.config_from_object('django.conf:settings')
# This line will tell Celery to autodiscover all your tasks.py that are in your app folders
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
