from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def notification(subject, message, recipient_email):
    """Отправка уведомление об обновлении курса/урока по электронной почте."""
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
    )
