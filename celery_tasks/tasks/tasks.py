from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_lesson_notification(lesson_id):
    from lessons.models import Lesson
    
    try:
        lesson = Lesson.objects.get(id=lesson_id)

        logger.info("Уведомление отправлено студенту %s по уроку '%s' (ID: %s)", lesson.student.id, lesson.title, lesson.id)

        return f"Уведомление для студента {lesson.student_id} отправлено"

    except Lesson.DoesNotExist:
        logger.error("Урок с ID %s не найден", lesson_id)
        return "Урок не найден"
