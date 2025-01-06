from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%B %d, %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'
