from celery import shared_task
from celery.task.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
import time

from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)


# @periodic_task(
#     run_every=(crontab(minute='*/15')),
#     name="task_save_latest_flickr_image",
#     ignore_result=True
# )
# def task_save_latest_flickr_image():
#     """
#     Saves latest image from Flickr
#     """
#     save_latest_flickr_image()
#     logger.info("Saved image from Flickr")

@shared_task
def sleepy(duration):
    time.sleep(duration)
    return None


# @shared_task
def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = 'Bienvenido, esto es un mensaje de prueba CELERY Y DJANGO'
    users = User.objects.filter(username='root')
    for user in users:
        time.sleep(1)
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER,
                  [user.email], fail_silently=False)
    return '{} se envio el correo correctamente'.format(user)
