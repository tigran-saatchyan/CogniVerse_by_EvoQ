from rest_framework import serializers

from payments.models import Payment


class PaymentsSerializer(serializers.ModelSerializer):

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
