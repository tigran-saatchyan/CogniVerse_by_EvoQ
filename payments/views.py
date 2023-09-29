import stripe
from django.conf import settings
from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from stripe.error import StripeError

from payments.models import Payment
from payments.serializers import PaymentsSerializer, CardInformationSerializer
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
            response = self.stripe_card_payment(
                data_dict=data_dict,
                product_price=product_price
            )

            self.save_payment_if_valid(response, payment)

        else:
            response = {
                'errors': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            }

        return Response(response)

    @staticmethod
    def stripe_card_payment(data_dict, product_price):
        try:
            card_details = {
                "type": "card",
                "card": {
                    "number": data_dict['card_number'],
                    "exp_month": data_dict['expiry_month'],
                    "exp_year": data_dict['expiry_year'],
                    "cvc": data_dict['cvc'],
                },
            }

            payment_intent = stripe.PaymentIntent.create(
                amount=product_price,
                currency='rub',
                payment_method="pm_card_visa",
                payment_method_types=[card_details["type"]],
                automatic_payment_methods={
                    "enabled": False,
                },
            )

            try:
                payment_confirm = stripe.PaymentIntent.confirm(
                    payment_intent['id']
                )
                payment_intent_modified = stripe.PaymentIntent.retrieve(
                    payment_intent['id']
                )
            except StripeError as e:
                print(e)
                payment_intent_modified = stripe.PaymentIntent.retrieve(
                    payment_intent['id']
                )
                payment_confirm = {
                    "stripe_payment_error": f"Failed with message: \n {e}",
                    "code": payment_intent_modified['last_payment_error'][
                        'code'],
                    "message": payment_intent_modified['last_payment_error'][
                        'message'],
                    'status': "Failed"
                }
            if (payment_intent_modified
                    and payment_intent_modified['status'] == 'succeeded'):
                response = {
                    'message': "Card Payment Success",
                    'status': status.HTTP_200_OK,
                    "card_details": card_details,
                    "payment_intent": payment_intent_modified,
                    "payment_confirm": payment_confirm
                }
            else:
                response = {
                    'message': "Card Payment Failed",
                    'status': status.HTTP_400_BAD_REQUEST,
                    "card_details": card_details,
                    "payment_intent": payment_intent_modified,
                    "payment_confirm": payment_confirm
                }
        except Exception as e:
            response = {
                'error': f"Your card number is incorrect: {e}",
                'status': status.HTTP_400_BAD_REQUEST,
                "payment_intent": {"id": "Null"},
                "payment_confirm": {'status': "Failed"}
            }
        return response

    @staticmethod
    def save_payment_if_valid(response, payment):
        if response['payment_confirm'] and response[
            'status'
        ] == status.HTTP_200_OK:
            payment_confirm = response['payment_confirm']

            payment_method = stripe.PaymentMethod.retrieve(
                payment_confirm['payment_method']
            )

            payment['paid_price'] = int(
                payment_confirm['amount_received']
            ) // 100,
            payment['payment_method'] = payment_method['type']

            # TODO: проверка об оплате проверяется на уровне базы
            #       (unique_togather).
            #       Добавить проверку об оплате на уровне Stripe

            Payment.objects.create(**payment)
