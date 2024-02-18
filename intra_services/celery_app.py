import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intra_services.settings')   # изменить имя приложения
app = Celery('intra_services')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()