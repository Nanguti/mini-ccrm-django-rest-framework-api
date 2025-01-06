from celery import shared_task
from .models import Reminder
from django.core.mail import send_mail  # Or use a custom notification system

@shared_task
def send_reminder(reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    send_mail(
        'Reminder: ' + reminder.message,
        reminder.message,
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    reminder.is_sent = True
    reminder.save()
