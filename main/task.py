from logging import exception
from celery_email_scheduler.celery import app
from .models import Profile
import datetime
from django.core.mail import send_mail
from django.conf import settings

@app.task(name='send_notification')
def send_notification():
    try:    
        time_thresold = datetime.now() - datetime.timedelta(hours = 2)
        profile_objs = Profile.objects.filter(is_verified=False, created_at__gte=time_thresold)


        for profile_obj in profile_objs:
            subject = "Please verify your account!"
            message = "Your account is still not verified, please do it asap, thanks!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [profile_obj.email]
            send_mail(subject, message, email_from, recipient_list)
    except exception as e:
        print(e)