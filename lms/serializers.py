from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson, Subscription

from .validators import Only_Youtube


class CourseSerializer(ModelSerializer):
    """Сериализатор курса."""

    lessons_total = SerializerMethodField()
    lessons = SerializerMethodField()
    subscription = SerializerMethodField()

    def get_lessons(self, course):
        """Получаем все уроки в курсе в приведенной ниже форме."""
        return [
            f"{lesson.title} - {lesson.description}"
            for lesson in course.lesson_set.all()
        ]

    def get_lessons_total(self, course):
        """Получаем всего уроков в курсе."""
        return course.lesson_set.count()

    def get_subscription(self, course):
        """Проверяем подписку пользователя на курс."""
        user = self.context.get("request").user
        return Subscription.objects.filter(user=user, course=course).exists()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "preview",
            "description",
            "lessons_total",
            "lessons",
            "owner",
            "subscription",
        )


class LessonSerializer(ModelSerializer):
    """Сериализатор урока."""

    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ("id", "title", "course", "description", "preview", "video", "owner")
        validators = (Only_Youtube(field="video"),)


class SubscriptionSerializer(ModelSerializer):
    """Сериализатор подписки."""

    class Meta:
        model = Subscription
        fields = ("user", "course")
