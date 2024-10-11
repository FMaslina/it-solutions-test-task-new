from django.urls import path

from cars.views import car_list_view, car_detail_view


urlpatterns = [
    path('cars/', car_list_view, name='car-list'),
    path('cars/<int:pk>', car_detail_view, name='car-detail')
]
