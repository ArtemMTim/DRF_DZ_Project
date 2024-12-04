from rest_framework.serializers import ModelSerializer
from lms.models import Course, Lesson

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description')

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'preview', 'video')