import json
from datetime import timedelta

from django_celery_beat.models import (
    PeriodicTask,
    CrontabSchedule,
)


def schedule_notification(course, update_time):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=update_time.minute,
        hour=update_time.hour + 4,
    )
    task = PeriodicTask.objects.filter(
        name=f'Notification - course_id: {course.pk}'
    ).first()
    if task:
        task.crontab = schedule
        task.save()
    else:
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Notification - course_id: {course.pk}',
            task='subscribers.tasks.course_update_notification',
            args=json.dumps([course.pk]),
            one_off=True,
            expires=update_time + timedelta(seconds=30)
        )
