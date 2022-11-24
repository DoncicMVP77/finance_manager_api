import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_manager.settings')

app = Celery('finance_manager')
# app.conf.enable_utc = False
# app.conf.update(timezone='Europe/Moscow')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

#Celery Beat Settings
app.conf.beat_schedule = {
    'send_statistic': {
        'task': 'manager.tasks.send_yesterday_user_statistic_on_email_task',
        'schedule': crontab(hour=8, minute=30, day_of_week=7),
    }
}
