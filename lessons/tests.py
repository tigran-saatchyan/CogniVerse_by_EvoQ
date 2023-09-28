from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from lessons.models import Lesson
from payments.models import Payment
from users.models import User


class LessonTestCase(APITestCase):
    """
    Test case for the Lesson API views.

    This test case includes test methods for creating, retrieving, listing,
    updating, and deleting lessons.
    It also tests URL validation within lesson descriptions and access
    control based on user permissions.

    Attributes:
        client (APIClient): The test client for making API requests.
        user (User): A test user for authentication.
        lesson1 (Lesson): A sample lesson with a valid YouTube URL in the
        description.
        lesson2 (Lesson): A sample lesson with an invalid URL in the
        description.

    Methods:
        test_create_lesson: Test the creation of a new lesson using POST.
        test_valid_url_in_description: Test creating a lesson with a valid
        YouTube URL in the description.
        test_invalid_url_in_description: Test creating a lesson with an
        invalid URL in the description.
        test_retrieve_lesson: Test retrieving a lesson by its ID.
        test_list_lessons: Test listing all lessons.
        test_update_lesson: Test updating a lesson by its ID.
        test_delete_lesson: Test deleting a lesson by its ID.

    Usage:
        - Use this test case to ensure the correctness of Lesson API views
        and their behavior.
    """

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
        """
        Test creating a new lesson using POST.

        This test verifies that a new lesson can be created successfully
        using a POST request.
        It checks the HTTP status code, the response data, and the existence
        of the created lesson.

        Request:
            - HTTP method: POST
            - Data: Lesson data in the request body.

        Response:
            - HTTP status: 201 Created on successful creation.
            - Data: The newly created lesson data.

        Usage:
            - Use this test to ensure that lessons can be created through
            the API.
        """
        # Test data for creating a lesson
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
        """
        Test creating a lesson with a valid YouTube URL in the description.

        This test verifies that a lesson can be created with a valid YouTube
        URL in the description.
        It checks the HTTP status code to ensure successful creation.

        Request:
            - HTTP method: POST
            - Data: Lesson data with a valid YouTube URL in the description.

        Response:
            - HTTP status: 201 Created on successful creation.

        Usage:
            - Use this test to ensure that lessons with valid YouTube URLs
            can be created.
        """
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
        """
        Test creating a lesson with an invalid URL in the description.

        This test verifies that a lesson with an invalid URL in the
        description is rejected,
        resulting in a 400 Bad Request response.

        Request:
            - HTTP method: POST
            - Data: Lesson data with an invalid URL in the description.

        Response:
            - HTTP status: 400 Bad Request.

        Usage:
            - Use this test to ensure that lessons with invalid URLs are
            rejected.
        """
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
        """
        Test retrieving a lesson by its ID.

        This test verifies that a lesson can be retrieved by its ID.
        It checks the HTTP status code and the expected data in the response.

        Usage:
            - Use this test to ensure that lessons can be retrieved by their
            ID.
        """
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
        """
        Test listing all lessons.

        This test verifies that all lessons can be listed.
        It checks the HTTP status code and the number of lessons in the
        response.

        Usage:
            - Use this test to ensure that all lessons can be listed.
        """
        url = reverse(
            'lessons:lesson-list'
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), 2
        )

    def test_update_lesson(self):
        """
        Test updating a lesson by its ID.

        This test verifies that a lesson can be updated by its ID.
        It checks the HTTP status code and whether the lesson data is
        updated correctly.

        Usage:
            - Use this test to ensure that lessons can be updated by their ID.
        """
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
        """
        Test deleting a lesson by its ID.

        This test verifies that a lesson can be deleted by its ID.
        It checks the HTTP status code and ensures that the lesson is no
        longer present in the database.

        Usage:
            - Use this test to ensure that lessons can be deleted by their ID.
        """
        url = reverse('lessons:lesson-destroy', args=[self.lesson2.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(id=self.lesson2.id)
