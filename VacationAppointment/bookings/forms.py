from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'departure_date', 'return_date', 'number_of_travelers']