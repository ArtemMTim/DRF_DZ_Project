from django.db import models


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        unique=True,
        help_text="Введите название курса",
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
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберите курс"
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
    video = models.URLField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title



