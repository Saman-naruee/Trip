from django.contrib.auth.models import Trip
from rest_framework import serializers

class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'