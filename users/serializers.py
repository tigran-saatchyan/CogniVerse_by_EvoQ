from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)

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
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
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
