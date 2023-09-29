from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course
from users.models import User


class PaymentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="testpassword"
        )

        self.course = Course.objects.create(
            title="Test Course", description="Test Course Description"
        )
        model_name = self.course.__class__.__name__.lower()

        self.payment_url = reverse(
            'payments:make_payment',
            args=[model_name, self.course.pk]
        )
        self.card_data = {
            "payment_method": "card",
            "card_number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvc": "123",
            "email": "test@gmail.com"
        }

    def test_make_payment(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            self.payment_url, self.card_data, format='json'
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_payment(self):
        response = self.client.post(
            self.payment_url, self.card_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
