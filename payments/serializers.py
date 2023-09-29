from rest_framework import serializers

from payments.models import Payment
from payments.validators import (
    check_expiry_month,
    check_expiry_year,
    check_cvc, check_payment_method, check_card_number,
)


class PaymentsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Payment model.

    This serializer is used to convert Payment model instances into JSON
    data and vice versa.
    It defines the fields to be included in the serialized representation of
    Payment objects.

    Attributes:
        model (Payment): The model class that this serializer is associated
        with.
        fields (tuple): The fields to include in the serialized representation.

    Usage:
        - Use this serializer to convert Payment model instances into JSON
        data for API responses.
        - Include this serializer in views that require serialization of
        Payment objects.

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
                    'paid_price',
                    'payment_method'
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
            'paid_price',
            'payment_method'
        )


class CardInformationSerializer(serializers.Serializer):
    payment_method = serializers.CharField(
        max_length=50,
        required=True,
        validators=[check_payment_method]
    )
    card_number = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_card_number]
    )
    expiry_month = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_month],
    )
    expiry_year = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_year],
    )
    cvc = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_cvc],
    )
