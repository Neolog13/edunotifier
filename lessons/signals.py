from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lesson
from celery_tasks.tasks.tasks import send_lesson_notification


@receiver(post_save, sender=Lesson)
def lesson_created_handler(sender, instance, created, **kwargs):
    if created:
        send_lesson_notification.delay(instance.id)
