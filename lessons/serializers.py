from rest_framework import serializers

from lessons.models import Lesson
from lessons.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Lesson model.

    This serializer is used to convert Lesson model instances into JSON data
    and vice versa.
    It defines the fields to be included in the serialized representation
    and includes a custom
    URL validation validator for the 'description' field.

    Attributes:
        model (Lesson): The model class that this serializer is associated
        with.
        fields (tuple): The fields to include in the serialized representation.
        validators (list): A list of validators to apply to the serializer's
        fields.

    Usage:
        - Use this serializer to convert Lesson model instances into JSON
        data for API responses.
        - Include this serializer in views that require serialization of
        Lesson objects.

    Example:
        ```python
        from rest_framework import serializers

        class MyLessonSerializer(LessonSerializer):
            # Additional custom fields or overrides can be added here.

            class Meta:
                model = Lesson
                fields = ('id', 'title', 'description', 'image', 'owner')
                validators = [UrlValidator(field='description')]
        ```
    """
    price = serializers.SerializerMethodField()

    @staticmethod
    def get_price(instance):
        return instance.price // 100

    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'description',
            'price',
            'course',
            'image',
            'owner'
        )
        validators = [UrlValidator(field='description')]


class LessonCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'description',
            'price',
            'course',
            'image',
            'owner'
        )
        read_only_fields = ['id', 'owner']
        validators = [UrlValidator(field='description')]

    def create(self, validated_data):
        validated_data['price'] = int(float(validated_data.pop('price')) * 100)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.price = int(float(validated_data.pop('price')) * 100)
        for field_name, new_value in validated_data.items():
            setattr(instance, field_name, new_value)
        instance.save()
        return instance

