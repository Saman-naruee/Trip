from django.urls import path
from . import views
from .views import make_trip, trip_update, delete_trip, list_trips

urlpatterns = [
    path('trips/new/', views.make_trip, name='make_trip'),
    path('trips/', views.trip_update, name='trip_update'),
    path('trips/<int:pk>/delete/', views.delete_trip, name='delete_trip'),
    path('trips/<int:pk>/edit/', views.trip_update, name='trip_update'),

]

# /trips/new/: URL برای ویوی ایجاد سفر.
# /trips/: URL برای ویوی لیست سفرها.
# /trips/<int:pk>/edit/: URL برای ویوی به‌روزرسانی سفر.
# /trips/<int:pk>/delete/: URL برای ویوی حذف سفر.