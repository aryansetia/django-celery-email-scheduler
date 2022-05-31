import os
from  django.conf import settings
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_email_scheduler.settings')

app = Celery('celery_email_scheduler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-2-hour':{
        'task': 'send_notification',
        'schedule': crontab(hour='*/2')
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')