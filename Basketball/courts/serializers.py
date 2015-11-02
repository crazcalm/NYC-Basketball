from rest_framework import serializers
from courts.models import Court

class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ('id', 'name', 'last_modified', 'location',
            'num_of_courts', 'accessible', 'longitude',
            'latitude')
