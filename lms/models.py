# from users.models import User
from django.conf import settings
from django.db import models


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        unique=True,
        help_text="Введите название курса",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец курса",
        help_text="Введите владельца курса",
    )
    preview = models.ImageField(
        upload_to="lms/previews",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец урока",
        help_text="Введите владельца урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="lms/previews",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    video = models.URLField(max_length=255, blank=True, null=True, verbose_name="Видео")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


class Subscription(models.Model):
    """Модель подписки"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.user} - {self.course}"
