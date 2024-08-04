from django.urls import path
from . import views
from .views import make_trip, trip_update, delete_trip, list_trips

urlpatterns = [
    path('trips/new/', views.make_trip, name='make_trip'),
    path('trips/', views.list_trips, name='list_trips'),
    path('trips/<int:id>/delete/', views.delete_trip, name='delete_trip'),
    path('trips/<int:id>/edit/', views.trip_update, name='trip_update'),

]

