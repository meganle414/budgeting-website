import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budgetingwebsite.settings')

app = Celery('budgetingwebsite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()