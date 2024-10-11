from django.urls import path

from cars.views import car_list_view

urlpatterns = [
    path('cars/', car_list_view, name='car-list'),
]
