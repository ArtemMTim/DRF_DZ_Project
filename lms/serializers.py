from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .validators import Only_Youtube
from lms.models import Course, Lesson
from rest_framework import serializers

class CourseSerializer(ModelSerializer):
    """Сериализатор курса."""
    lessons_total = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        # return [f'{lesson.title} - {lesson.description}' for lesson in Lesson.objects.filter(course=course)]
        return [
            f"{lesson.title} - {lesson.description}"
            for lesson in course.lesson_set.all()
        ]

    def get_lessons_total(self, course):
        return course.lesson_set.count()

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
        )


class LessonSerializer(ModelSerializer):
    """Сериализатор урока."""
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ("id", "title", "course", "description", "preview", "video", "owner")
        validators = (Only_Youtube(field="video"),)
