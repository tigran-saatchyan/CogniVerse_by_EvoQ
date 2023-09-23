import re

from rest_framework.exceptions import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        unvalidated_field = dict(value).get(self.field)

        basic_url_pattern = r'(https?://)?(www\.)?([a-zA-Z0-9\-\_]+\.[a-zA-Z]{1,4})'
        valid_url_pattern = r'^(https?://)?(www\.)?(youtube\.com\/?|youtu\.be\/?)'

        urls = re.findall(basic_url_pattern, unvalidated_field)

        for url in urls:
            url = ''.join(url)
            if not bool(re.match(valid_url_pattern, url)):
                raise ValidationError('Only YouTube URLs are allowed')
