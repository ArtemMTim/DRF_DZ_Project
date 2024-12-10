from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
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
        fields = ("id", "title", "preview", "description", "lessons_total", "lessons")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "title", "description", "preview", "video")
