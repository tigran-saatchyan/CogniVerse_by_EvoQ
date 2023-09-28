from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course
from users.models import User
from .models import Subscriber


class SubscribeViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='user@test.test', password='test'
        )

        self.course = Course.objects.create(
            title="Test Course", description="Test Course Description"
        )

        self.url = reverse("subscribers:subscribe", args=[self.course.id])

    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Subscribed successfully")
        self.assertTrue(
            Subscriber.objects.filter(
                user=self.user, course=self.course
            ).exists()
        )

    def test_unsubscribe_from_course(self):
        self.client.force_authenticate(user=self.user)
        self.subscriber = Subscriber.objects.create(
            user=self.user, course=self.course
        )
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Unsubscribed successfully")
        self.assertFalse(
            Subscriber.objects.filter(
                user=self.user, course=self.course
            ).exists()
        )

    def test_unauthorized_subscribe(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_course_id(self):
        self.client.force_authenticate(user=self.user)
        invalid_url = reverse(
            "subscribers:subscribe", args=[999]
        )
        response = self.client.post(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
