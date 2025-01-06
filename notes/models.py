from django.db import models
from leads.models import Lead
from contacts.models import Contact  # If Contact needs to be referenced

class Note(models.Model):
    lead = models.ForeignKey(
        Lead, 
        related_name='notes', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True 
    )
    contact = models.ForeignKey(
        'contacts.Contact', 
        related_name='notes', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {'Lead' if self.lead else 'Contact'}: {self.content[:50]}"
