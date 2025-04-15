from __future__ import absolute_import, unicode_literals
import os
from celery_config import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_management.settings')

app = Celery('product_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()