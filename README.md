### Prerequisites
To run the app, first install all the requirments using
```pip install -r requirments```
in a virtual enviroment.

Setup the email backend
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
```
### To run
Run the django server as localhost
```python
python manage.py runserver
```
Start a Celery worker service 
```python
celery -A celery_email_scheduler worker --loglevel=info
```
As a separate process, start the celery beat service
```python
celery -A celery_email_scheduler beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
