from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from .models import Reminder

@shared_task
def send_reminder_email(reminder_id):
    try:
        # Get the reminder from the database
        reminder = Reminder.objects.get(id=reminder_id)
        message = f"Hello, this is a reminder: {reminder.message}"
        send_mail(
            subject="Reminder Notification",
            message=message,
            from_email="g.nanguti@gmail.com",
            recipient_list=[reminder.contact.email],
        )
        return f"Reminder email sent to {reminder.contact.email}"
    except Reminder.DoesNotExist:
        return "Reminder does not exist"
    
@shared_task
def schedule_reminders():
    now = datetime.now()
    reminders = Reminder.objects.filter(remind_at__lte=now, sent=False)

    for reminder in reminders:
        # Mark as sent
        reminder.sent = True
        reminder.save()
        send_reminder_email.delay(reminder.id)
