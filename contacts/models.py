from django.db import models
from leads.models import Lead

class Contact(models.Model):
    lead = models.ForeignKey(Lead, related_name='contacts', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        """
        Return a string representation of this Contact.
        
        This is the name of the contact.
        """
        return self.name
