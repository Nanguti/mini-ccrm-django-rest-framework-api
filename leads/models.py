from django.db import models

# Create leads model for the crm, where I have the following classes: Leead, Contact, Note and Reminder

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """
        Return a string representation of this Lead.

        This is the name of the lead.
        """
        return self.name