from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import TripForm

def make_trip(request):
    context = {
        'form' : form,
    }
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('trip_success')
    else:
        form = TripForm()
    
    return render(request, 'maketrip.html', context)



# git checkout feature-branch
# git pull origin feature-branch
