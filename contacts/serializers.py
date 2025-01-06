from rest_framework import serializers
from .models import Contact
from leads.models import Lead

class ContactSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(
        queryset=Lead.objects.all(),
        allow_null=True,
        required=False
    )  # This is for input in the DRF GUI
    lead_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['lead_name']

    def get_lead_name(self, obj):
        """Return the name of the lead if assigned, otherwise None."""
        return obj.lead.name if obj.lead else None
