from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия"
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        verbose_name="Тип пользователя",
        default='student'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_display_name(self):
        user_type_display = dict(self.USER_TYPE_CHOICES).get(self.user_type, '')

        name_parts = [self.last_name, self.first_name]

        full_name = ' '.join(name_parts)
        return f"{user_type_display} {full_name}".strip()

    def __str__(self):
        return self.get_display_name()
    