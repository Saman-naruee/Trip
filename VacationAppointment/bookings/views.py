from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import TripForm
from django.urls import reverse_lazy
from .models import Trip

def make_trip(request):
    context = {
        'form' : TripForm,
    }
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_trips')
    else:
        form = TripForm()
    return render(request, 'bookings/create_trip.html', context)


def list_trips(request):
    context = {
        'trips' : Trip.objects.all(),
    }
    path = 'bookings/list_trips.html'
    return render(request, path, context)


def trip_update(request, id):
    path = 'bookings/update_trip.html' 
    trip = get_object_or_404(Trip, id = id)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect(list_trips)
    else:
        form = TripForm(instance=trip)
    context = {
        'form' : form,
    }
    return render(request, path, context)
    

def delete_trip(request, id):
    path = 'bookings/confirm_delete.html' 
    trip = get_object_or_404(Trip, id = id)
    if request.method == 'POST':
        trip.delete()
        return redirect(list_trips)
    return render(request, path, context={'trip', 'trip'})