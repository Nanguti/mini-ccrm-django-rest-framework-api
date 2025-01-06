from rest_framework import serializers
from .models import Note
from leads.models import Lead
from contacts.models import Contact

class NoteSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(
        queryset=Lead.objects.all(),
        required=False,
        allow_null=True
    )  # Allow selection of a lead
    lead_name = serializers.SerializerMethodField()  # Display lead name in the response
    contact = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True
    )  # Allow selection of a contact
    contact_name = serializers.SerializerMethodField()  # Display contact name in the response
    created_at = serializers.DateTimeField(format="%B %d, %Y, %I:%M %p", read_only=True)  

    class Meta:
        model = Note
        fields = ['id', 'lead', 'lead_name', 'contact', 'contact_name', 'content', 'created_at']
        read_only_fields = ['created_at']  # Ensure created_at is not editable

    def get_lead_name(self, obj):
        """Return the name of the lead if it exists, otherwise None."""
        return obj.lead.name if obj.lead else None

    def get_contact_name(self, obj):
        """Return the name of the contact if it exists, otherwise None."""
        return obj.contact.name if obj.contact else None
