from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_trip, name='make_trip'),
]
