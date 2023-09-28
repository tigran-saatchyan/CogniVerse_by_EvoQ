from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from courses.models import Course
from users.models import User
from .models import Subscriber


class SubscribeViewTests(APITestCase):
    """
    Test cases for the SubscribeView.

    These test cases cover the functionality of subscribing and
    unsubscribing from a course
    using the SubscribeView. They test both successful and error scenarios.

    Attributes:
        client (APIClient): The client for making API requests.
        user (User): The user for testing authentication.
        course (Course): The course for testing subscription.
        url (str): The URL for making subscription requests.

    Methods:
        test_subscribe_to_course(): Test subscribing to a course and the
        expected response.
        test_unsubscribe_from_course(): Test unsubscribing from a course and
        the expected response.
        test_unauthorized_subscribe(): Test unauthorized subscription and
        the expected response.
        test_invalid_course_id(): Test subscribing with an invalid course ID
        and the expected response.

    Usage:
        - Use this test class to validate the behavior of the SubscribeView
        in your Django REST framework API.
    """

    def setUp(self):
        """
        Set up test data and URL for testing.

        This method prepares the necessary data and URL for testing
        subscription behavior.
        It includes creating a test user, a test course, and constructing
        the subscription URL.
        """
        self.client = APIClient()
        self.user = User.objects.create(
            email='user@test.test', password='test'
        )
        self.course = Course.objects.create(
            title="Test Course", description="Test Course Description"
        )
        self.url = reverse("subscribers:subscribe", args=[self.course.id])

    def test_subscribe_to_course(self):
        """
        Test subscribing to a course and the expected response.

        This test case simulates a successful subscription to a course and
        checks that
        the response status code is 201 (Created) and the message indicates
        successful subscription.
        It also verifies that a Subscriber record for the user and course
        exists.
        """
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
        """
        Test unsubscribing from a course and the expected response.

        This test case simulates a successful unsubscription from a course
        and checks that
        the response status code is 200 (OK) and the message indicates
        successful unsubscription.
        It also verifies that the Subscriber record for the user and course
        no longer exists.
        """
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
        """
        Test unauthorized subscription and the expected response.

        This test case simulates a subscription request without
        authentication and checks that
        the response status code is 401 (Unauthorized).
        """
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_course_id(self):
        """
        Test subscribing with an invalid course ID and the expected response.

        This test case simulates a subscription request with an invalid
        course ID and checks that
        the response status code is 404 (Not Found).
        """
        self.client.force_authenticate(user=self.user)
        invalid_url = reverse(
            "subscribers:subscribe", args=[999]
        )
        response = self.client.post(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
