from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models import Course
from .models import Subscriber

from .serializers import SubscriberSerializer


class SubscribeView(APIView):
    def post(self, request, course_id):
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
