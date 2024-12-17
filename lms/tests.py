from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="Test_course", owner=self.user)
        self.lesson = Lesson.objects.create(
            title="Test_lesson", owner=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        url = reverse("lms:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.id,
                    "title": self.lesson.title,
                    "course": {
                        "id": self.course.id,
                        "title": self.course.title,
                        "preview": None,
                        "description": None,
                        "lessons_total": 1,
                        "lessons": [f"{self.lesson.title} - None"],
                        "owner": self.user.id,
                        "subscription": False,
                    },
                    "description": None,
                    "preview": None,
                    "video": None,
                    "owner": self.user.id,
                }
            ],
        }
        self.assertEqual(response.json(), result)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_retrieve", args=(self.lesson.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("title")
        self.assertEqual(result, self.lesson.title)

    def test_lesson_create(self):
        data = {"title": "New_test", "course": 1}
        url = reverse("lms:lesson_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lesson_update", args=(self.lesson.id,))
        data = {"title": "New_title"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("title")
        self.assertEqual(result, data.get("title"))

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="Test_course", owner=self.user)
        #self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)
    def test_subscription(self):
        data = {"course": self.course.pk}
        url = reverse("lms:subscription")
        print(f"URL: {url}")
        print(f"Data: {data}")

        response = self.client.post(url, data=data)
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.json()}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)






