import datetime

from rest_framework import serializers

from payments.models import Payment


def check_expiry_month(value):
    try:
        if not 1 <= int(value) <= 12:
            raise serializers.ValidationError("Invalid expiry month.")
    except ValueError:
        raise serializers.ValidationError(
            "Must be string representing integer. "
            "Ex.: '08' for August"
        )


def check_expiry_year(value):
    today = datetime.datetime.now()

    try:
        if not int(value) >= today.year:
            raise serializers.ValidationError("Invalid expiry year.")
    except ValueError:
        raise serializers.ValidationError(
            "Must be string representing integer. "
            "Ex.: '2023', '2022'"
        )


def check_card_number(value):
    def digits_of(substring):
        return [int(char) for char in str(substring)]

    digits = digits_of(value)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    if checksum % 10 != 0:
        raise serializers.ValidationError("Invalid card number.")


def check_cvc(value):
    if not 3 <= len(value) <= 4:
        raise serializers.ValidationError("Invalid cvc number.")


def check_payment_method(value):
    payment_method = value.lower()
    if payment_method not in ["card"]:
        raise serializers.ValidationError("Invalid payment_method.")


def product_owner_validation(item):

    if Payment.objects.get(**item).exists():
        raise serializers.ValidationError('You already bought this product')
