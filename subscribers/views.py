from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscribeView(APIView):
    """
    View for subscribing and unsubscribing from a course.

    This view allows users to subscribe to or unsubscribe from a specific
    course. If a user is already
    subscribed to the course, clicking the subscribe button will unsubscribe
    them, and vice versa.

    HTTP Methods:
        - POST: Subscribes or unsubscribes the user from the specified course.

    Attributes:
        None

    Methods:
        post(request, course_id): Handles the POST request to subscribe or
        unsubscribe the user from the course.

    Usage:
        - Include this view in your Django REST framework API to enable user
        subscription functionality.
    """

    def post(self, request, course_id):
        """
        Handle POST request to subscribe or unsubscribe from a course.

        Args:
            request (Request): The HTTP request object.
            course_id (int): The ID of the course to subscribe or
            unsubscribe from.

        Returns:
            Response: A response indicating success or failure of the
            subscription action.

        Usage:
            - Use this method to subscribe or unsubscribe users from a
            specific course.
        """
        user = request.user
        try:
            subscriber = Subscriber.objects.get(user=user, course=course_id)
            subscriber.delete()
            return Response(
                {"message": "Unsubscribed successfully"},
                status=status.HTTP_200_OK
            )
        except Subscriber.DoesNotExist:
            serializer = SubscriberSerializer(
                data={"user": user.pk, "course": course_id}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Subscribed successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors, status=status.HTTP_404_NOT_FOUND
            )
