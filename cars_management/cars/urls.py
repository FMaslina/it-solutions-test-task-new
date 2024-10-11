from django.urls import path

from cars.views import car_list_view, car_detail_view, car_create_view, car_edit, car_delete


urlpatterns = [
    path('', car_list_view, name='car-list'),
    path('<int:pk>', car_detail_view, name='car-detail'),
    path('creation', car_create_view, name='car-create'),
    path('car/<int:pk>/edit/', car_edit, name='car-edit'),
    path('car/<int:pk>/delete/', car_delete, name='car-delete'),
]
