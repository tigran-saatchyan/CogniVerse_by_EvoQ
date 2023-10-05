from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def activity_check():
    due_date = timezone.now() - timedelta(days=30)
    queryset = User.objects.filter(last_login__lte=due_date)
    queryset.update(is_active=False)
