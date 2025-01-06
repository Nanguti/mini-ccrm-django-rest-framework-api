from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Create an interval schedule
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.MINUTES,  # Run every 1 minute
)

# Create the periodic task
PeriodicTask.objects.create(
    interval=schedule,
    name="Schedule Reminder Emails",
    task="reminders.tasks.schedule_reminders",
)
