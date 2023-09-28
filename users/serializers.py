from rest_framework import serializers

from payments.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to convert User model instances into JSON data
    and vice versa.
    It defines the fields to be included in the serialized representation of
    User objects.

    Attributes:
        model (User): The model class that this serializer is associated with.
        fields (tuple): The fields to include in the serialized representation.

    Methods:
        to_representation(instance): Custom method to conditionally include
        or exclude fields based on the request user.

    Usage:
        - Use this serializer to convert User model instances into JSON data
        for API responses.
        - Customize the 'to_representation' method to conditionally include
        or exclude fields based on user roles.

    Example:
        ```python
        from rest_framework import serializers

        class MyUserSerializer(UserSerializer):
            # Additional custom fields or overrides can be added here.

            class Meta:
                model = User
                fields = (
                    'pk',
                    'email',
                    'first_name',
                    'last_name',
                    'telephone',
                    'image',
                    'country',
                    'city',
                    'payments',
                )
        ```
    """

    email = serializers.CharField(read_only=True)
    payments = PaymentsSerializer(source="payment", many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'first_name',
            'last_name',
            'telephone',
            'image',
            'country',
            'city',
            'payments',
        )

    def to_representation(self, instance):
        user = self.context['request'].user
        is_owner = user == instance
        data = super().to_representation(instance)

        if not is_owner:
            data.pop('payments', None)
            data.pop('last_name', None)
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    This serializer is used for creating new user accounts during the
    registration process.

    Attributes:
        model (User): The model class that this serializer is associated with.
        fields (tuple): The fields to include in the serialized representation.

    Methods:
        validate(data): Custom method to validate password confirmation
        during registration.
        create(validated_data): Custom method to create a new user account.

    Usage:
        - Use this serializer for user registration and account creation in
        your API.
    """

    pk = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)
    date_added = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'telephone',
            'image',
            'country',
            'city',
            'is_verified',
            'date_added',
            'date_modified',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            **validated_data
        )
        return user
