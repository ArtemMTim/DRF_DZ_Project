from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            title="Test_course", description="Test_course", owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title="Test_lesson", description="Test_lesson", owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(reverse("lms:lesson_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
