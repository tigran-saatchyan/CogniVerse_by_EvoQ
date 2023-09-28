import re
from rest_framework.exceptions import ValidationError


class UrlValidator:
    """
    Custom validator for validating URL fields.

    This validator is used to ensure that a URL field in a serializer meets
    specific criteria.
    It checks if the URL is a valid YouTube URL, allowing only YouTube links.

    Args:
        field (str): The name of the field to be validated.

    Usage:
        - Create an instance of this validator and pass the name of the URL
        field to be validated.
        - Include this validator in the `validators` list of the
        serializer's Meta class.

    Example:
        ```python
        from rest_framework import serializers

        class MySerializer(serializers.ModelSerializer):
            video_url = serializers.URLField(validators=[UrlValidator(
            field='video_url')])

            class Meta:
                model = MyModel
                fields = ('video_url',)
        ```

    Note:
        - This validator uses regular expressions to validate URLs.
        - It specifically checks if the URL is a valid YouTube URL.
        - If the URL doesn't match the YouTube pattern, a ValidationError is
        raised.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        unvalidated_field = dict(value).get(self.field)

        basic_url_pattern = (r'(https?://)?(www\.)?([a-zA-Z0-9\-\_]+\.['
                             r'a-zA-Z]{1,4})')
        valid_url_pattern = (r'^(https?://)?(www\.)?('
                             r'youtube\.com\/?|youtu\.be\/?)')

        urls = re.findall(basic_url_pattern, unvalidated_field)

        for url in urls:
            url = ''.join(url)
            if not bool(re.match(valid_url_pattern, url)):
                raise ValidationError('Only YouTube URLs are allowed')
