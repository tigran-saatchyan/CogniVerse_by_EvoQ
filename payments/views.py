from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.serializers import PaymentsSerializer


class PaymentsListView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payment.objects.all()

    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]

    filterset_fields = ['payment_type', 'course', 'lesson']
    ordering_fields = ['payment_date']
