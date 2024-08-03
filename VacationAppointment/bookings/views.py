from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import TripForm


def make_trip(request):
    context = {
        'form' : TripForm,
    }
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('trip_success')
    else:
        form = TripForm()
    
    return render(request, 'templates/bookings/maketrip.html', context)

def trip_list(request):
    pass

class TripUpdate():
    pass

class DeleteTrip():
    pass



# git checkout feature-branch
# git pull origin feature-branch
