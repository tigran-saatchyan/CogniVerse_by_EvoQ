from rest_framework import serializers
from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subscriber model.

    This serializer is used to convert Subscriber model instances into JSON
    data and vice versa.
    It defines the fields to be included in the serialized representation of
    Subscriber objects.

    Attributes:
        model (Subscriber): The model class that this serializer is
        associated with.
        fields (tuple): The fields to include in the serialized representation.

    Usage:
        - Use this serializer to convert Subscriber model instances into
        JSON data for API responses.
        - Include this serializer in views that require serialization of
        Subscriber objects.

    Example:
        ```python
        from rest_framework import serializers

        class MySubscriberSerializer(SubscriberSerializer):
            # Additional custom fields or overrides can be added here.

            class Meta:
                model = Subscriber
                fields = (
                    'user',
                    'course'
                )
        ```
    """

    class Meta:
        model = Subscriber
        fields = (
            'user',
            'course'
        )
