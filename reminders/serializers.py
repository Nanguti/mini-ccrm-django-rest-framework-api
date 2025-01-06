from rest_framework import serializers
from .models import Reminder
from leads.models import Lead
from contacts.models import Contact

class ReminderSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(
        queryset=Lead.objects.all(),
        allow_null=True,
        required=False
    )  # Write-enabled field
    lead_name = serializers.SerializerMethodField(read_only=True)
    contact = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        allow_null=True,
        required=False
    )
    contact_name = serializers.SerializerMethodField(read_only=True)
    remind_at = serializers.DateTimeField(format="%B %d, %Y, %I:%M %p")


    class Meta:
        model = Reminder
        fields = ['id', 'lead', 'lead_name', 'contact', 'contact_name', 'message', 'remind_at', 'is_sent']
        read_only_fields = ['lead_name', 'contact_name']

    def get_lead_name(self, obj):
        """Return the name of the lead, or None if the lead is not assigned."""
        return obj.lead.name if obj.lead else None

    def get_contact_name(self, obj):
        """Return the name of the contact, or None if the contact is not assigned."""
        return obj.contact.name if obj.contact else None

    def validate(self, data):
        # Ensure at least one of lead or contact is provided
        if not data.get('lead') and not data.get('contact'):
            raise serializers.ValidationError("Either 'lead' or 'contact' must be provided.")
        return data
