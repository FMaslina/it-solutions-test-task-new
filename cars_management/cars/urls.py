from django.urls import path

from cars.views import car_list_view, car_detail_view


urlpatterns = [
    path('', car_list_view, name='car-list'),
    path('<int:pk>', car_detail_view, name='car-detail')
]
