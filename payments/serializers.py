from rest_framework import serializers
from payments.models import Payment

class PaymentsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Payment model.

    This serializer is used to convert Payment model instances into JSON data and vice versa.
    It defines the fields to be included in the serialized representation of Payment objects.

    Attributes:
        model (Payment): The model class that this serializer is associated with.
        fields (tuple): The fields to include in the serialized representation.

    Usage:
        - Use this serializer to convert Payment model instances into JSON data for API responses.
        - Include this serializer in views that require serialization of Payment objects.

    Example:
        ```python
        from rest_framework import serializers

        class MyPaymentsSerializer(PaymentsSerializer):
            # Additional custom fields or overrides can be added here.

            class Meta:
                model = Payment
                fields = (
                    'user',
                    'payment_date',
                    'course',
                    'lesson',
                    'payed_price',
                    'payment_type'
                )
        ```
    """

    class Meta:
        model = Payment
        fields = (
            'user',
            'payment_date',
            'course',
            'lesson',
            'payed_price',
            'payment_type'
        )
