from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from lms.models import Course, Subscription


@shared_task
def notification(course_object_id, course_object_title):
    """Отправка уведомление об обновлении курса/урока по электронной почте.
    Принимает id курса и уго название. Формирует тему письма и его текст. Формирует список получателей и отправляет письмо."""
    subject = f"Обновление курса {course_object_title}"
    message = f"Здравствуйте!\nКурс {course_object_title} был обновлён. Ознакомьтесь с обновлением.\nС Уважением, администрация сервиса!"
    courses = Subscription.objects.filter(course=course_object_id)
    recipient_emails = [course.user.email for course in courses]
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_emails
    )
