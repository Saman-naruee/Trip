from django import forms
'destination، departure_date، return_date و number_of_travelers'
class TripForm(forms.Form):
    destination = forms.CharField(max_length=300)
    departure_date = forms.CharField(max_length=300)
    return_date = forms.DateField()
    number_of_travelers = forms.IntegerField()
