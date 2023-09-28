from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lessons.models import Lesson
from payments.models import Payment
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='user@test.test', password='test'
        )
        self.client.force_authenticate(user=self.user)

        self.lesson1 = Lesson.objects.create(
            title="Lesson 1",
            description="YouTube URL: https://www.youtube.com/watch?v=video1",
            owner=self.user
        )
        self.lesson2 = Lesson.objects.create(
            title="Lesson 2",
            description="Invalid URL: https://example.com",
            owner=self.user
        )

    def test_create_lesson(self):
        test_data = {
            'id': 3,
            'title': 'Test Lesson',
            'description': 'Lorem ipsum dolor sit amet.',
            'image': None,
            'owner': 1
        }
        url = reverse('lessons:lesson-create')

        response = self.client.post(
            path=url,
            data={
                'title': 'Test Lesson',
                'description': 'Lorem ipsum dolor sit amet.'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            test_data
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_valid_url_in_description(self):
        data = {
            "title": "Valid URL Lesson",
            "description": "YouTube URL: "
                           "https://www.youtube.com/watch?v=video3"
        }
        url = reverse(
            'lessons:lesson-create'
        )
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_url_in_description(self):
        data = {
            "title": "Invalid URL Lesson",
            "description": "Invalid URL: https://example.com"
        }
        url = reverse(
            'lessons:lesson-create'
        )
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_lesson(self):
        Payment.objects.create(
            user=self.user,
            lesson=self.lesson1,
            payed_price=60000,
            payment_type='cash'
        )

        url = reverse(
            'lessons:lesson-retrieve', args=[self.lesson1.id]
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = {
            "id": self.lesson1.id,
            "title": self.lesson1.title,
            "description": self.lesson1.description,
            "image": None,
            "owner": self.lesson1.owner.pk
        }

        self.assertEqual(response.data, expected_data)

    def test_list_lessons(self):
        url = reverse(
            'lessons:lesson-list'
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), 2
        )

    def test_update_lesson(self):
        updated_data = {
            "title": "Updated Lesson",
            "description": "Updated description"
        }

        url = reverse(
            'lessons:lesson-update', args=[self.lesson1.id]
        )

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_lesson = Lesson.objects.get(id=self.lesson1.id)
        self.assertEqual(updated_lesson.title, updated_data['title'])
        self.assertEqual(
            updated_lesson.description, updated_data['description']
        )

    def test_delete_lesson(self):
        url = reverse('lessons:lesson-destroy', args=[self.lesson2.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(id=self.lesson2.id)
