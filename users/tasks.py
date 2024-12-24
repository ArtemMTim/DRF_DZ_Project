from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def user_last_login():
    """Проверяет время последнего login в сервисе.
    Если пользователь не логинился никогда, либо более 30 дней назад, делает его неактивным
    """
    today = timezone.now().date()
    users = User.objects.all()
    for user in users:
        if not user.last_login:
            user.is_active = False
            user.save()
        elif today - user.last_login.date() > timedelta(days=30):
            user.is_active = False
            user.save()
