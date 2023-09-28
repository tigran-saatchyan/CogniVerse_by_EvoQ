from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.serializers import PaymentsSerializer


class PaymentsListView(generics.ListAPIView):
    """
    List view for payments with filtering and ordering options.

    This view provides a list of payments, allowing clients to filter and
    order the results.
    It uses the Django Filters and OrderingFilter to provide filtering and
    ordering capabilities.

    Attributes:
        serializer_class: The serializer class used to serialize Payment
        model instances.
        queryset: The query set of Payment model instances to be displayed
        in the list view.
        filter_backends: A list of filter backend classes, including
        DjangoFilterBackend and OrderingFilter.
        filterset_fields: Fields on which clients can filter the payments.
        ordering_fields: Fields on which clients can order the payments.

    Usage:
        - Use this view to expose a list of payments with filtering and
        ordering options in your API.
        - Include this view in your Django REST framework API views and
        configure it as needed.

    Example:
        ```python
        from rest_framework import generics
        from payments.models import Payment
        from payments.serializers import PaymentsSerializer

        class MyPaymentsListView(PaymentsListView):
            # Additional customizations or overrides can be added here.

            class Meta(PaymentsListView.Meta):
                queryset = Payment.objects.filter(status='completed')
                ordering_fields = ['payment_date', 'amount']
        ```
    """

    serializer_class = PaymentsSerializer
    queryset = Payment.objects.all()

    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]

    filterset_fields = ['payment_type', 'course', 'lesson']
    ordering_fields = ['payment_date']
