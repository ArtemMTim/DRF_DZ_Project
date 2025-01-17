from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    """Модель пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        blank=True,
        null=True,
        help_text="Введите Ваше имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        blank=True,
        null=True,
        help_text="Введите Вашу фамилию",
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите Ваш аватар",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город проживания",
        blank=True,
        null=True,
        help_text="Введите Ваш город проживания",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Модель оплаты"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    payment_date = models.DateField(
        verbose_name="Дата оплаты",
        help_text="Введите дату оплаты",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        help_text="Введите название оплаченного курса",
        null=True,
        blank=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        help_text="Введите название оплаченного урока",
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        verbose_name="Сумма оплаты",
        max_digits=10,
        decimal_places=2,
        help_text="Введите сумму оплаты",
        null=True,
        blank=True,
    )
    session_id = models.CharField(
        max_length=255, verbose_name="ID сессии", blank=True, null=True
    )
    link_to_pay = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", blank=True, null=True
    )

    CASH = "наличная оплата"
    NON_CASH = "безналичная оплата"
    PAYMENT_CHOICES = [(CASH, "наличная оплата"), (NON_CASH, "безналичная оплата")]
    payment_method = models.CharField(
        verbose_name="Метод оплаты",
        max_length=100,
        help_text="Введите метод оплаты",
        choices=PAYMENT_CHOICES,
        default=CASH,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    # def __str__(self):
    # return f"{self.user.email} - {self.payment_date} - {self.payment_method}"
