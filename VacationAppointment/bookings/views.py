from django.shortcuts import render
from .forms import InputForm

def MakeTrip(request):
    path = 'maketrip.html'
    context = {
        'form' : InputForm(),
    }
    return render(request, path, context)

