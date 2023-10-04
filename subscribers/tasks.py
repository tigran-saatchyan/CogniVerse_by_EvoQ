from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse

from courses.models import Course
from subscribers.models import Subscriber


@shared_task
def send_notification(recipient_email, message, subject):
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[recipient_email],
        html_message=message,
    )


@shared_task
def course_update_notification(course_pk):
    print('Task activated')
    course = Course.objects.get(pk=course_pk)
    users_to_notify = Subscriber.objects.filter(course=course)
    recipient_email_list = [
        subscriber.user.email for subscriber in users_to_notify
    ]
    subject = f'Course - {course.title} Update Notification'
    message = (
        f'''
        <p>The course - <strong>{course.title.title()}</strong>, you are subscribed for 
        is updated recently, at {course.date_modified}.</p>
        <p>Follow this link to the updated course:
        <a href="{reverse("courses:courses-detail", args=[course.pk])}">
            {course.pk} - {course.title.title()} 
        </a>
        </p>
        '''
    )
    for recipient_email in recipient_email_list:
        send_notification.delay(recipient_email, message, subject)
