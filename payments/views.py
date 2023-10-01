import stripe
from django.conf import settings
from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import Payment
from payments.serializers import PaymentsSerializer, CardInformationSerializer
from payments.services import stripe_card_payment, save_payment_if_valid
from payments.validators import product_owner_validation


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

    filterset_fields = ['payment_method', 'course', 'lesson']
    ordering_fields = ['payment_date']


class PaymentAPI(APIView):
    serializer_class = CardInformationSerializer

    def post(self, request, model_name, model_id):
        from django.apps import apps

        model = apps.get_model(
            app_label=f'{model_name.lower()}s',
            model_name=model_name.title()
        )
        product = model.objects.get(id=model_id)
        payment = {
            'user': request.user,
            f'{model_name}': product
        }

        product_owner_validation(payment)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            stripe.api_key = settings.STRIPE_SECRET_KEY
            data_dict = serializer.data

            product_price = product.price
            response = stripe_card_payment(
                data_dict=data_dict,
                product_price=product_price
            )

            save_payment_if_valid(response, payment)

        else:
            response = {
                'errors': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            }

        return Response(response)
