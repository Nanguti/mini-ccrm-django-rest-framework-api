from django.db import models
from leads.models import Lead
from contacts.models import Contact  # Import Contact model

class Reminder(models.Model):
    lead = models.ForeignKey(Lead, related_name='reminders', on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.ForeignKey(Contact, related_name='reminders', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {'Lead' if self.lead else 'Contact'}: {self.message}"
