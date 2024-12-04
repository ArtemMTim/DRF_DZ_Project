from rest_framework.serializers import ModelSerializer, SerializerMethodField
from lms.models import Course, Lesson

class CourseSerializer(ModelSerializer):
    lessons_total = SerializerMethodField()

    def get_lessons_total(self, course):
        return course.lesson_set.count()
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons_total')

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'preview', 'video')