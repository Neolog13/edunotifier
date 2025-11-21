from django.utils import timezone
from django.db import models

from users.models import User


class Lesson(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('confirmed', 'Подтвержден'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="Название урока"
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lessons_as_student',
        limit_choices_to={'user_type': 'student'},
        verbose_name="Студент"
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lessons_as_teacher', 
        limit_choices_to={'user_type': 'teacher'},
        verbose_name="Преподаватель"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='created',
        verbose_name="Статус"
    )
    scheduled_at = models.DateTimeField(
        verbose_name="Запланировано на"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['-scheduled_at']

    def __str__(self):
        scheduled_dt = timezone.localtime(self.scheduled_at)
        date_str = scheduled_dt.strftime('%d.%m.%Y %H:%M')

        return f"{self.title} - {self.student} - {self.teacher} - {date_str}"

    def confirm(self):
        if self.status == 'created':
            self.status = 'confirmed'
            self.save()

            return True
        return False
