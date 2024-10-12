from django.urls import path

from cars.api import CarListCreateApiView, CarRetrieveUpdateDestroyApiView, CommentListCreateApiView
from cars.views import car_list_view, car_detail_view, car_create_view, car_edit, car_delete


urlpatterns = [
    path('', car_list_view, name='car-list'),
    path('<int:pk>', car_detail_view, name='car-detail'),
    path('creation', car_create_view, name='car-create'),
    path('<int:pk>/edit/', car_edit, name='car-edit'),
    path('<int:pk>/delete/', car_delete, name='car-delete'),
    path('api/cars', CarListCreateApiView.as_view(), name='car-list-create-api'),
    path('api/cars/<int:pk>', CarRetrieveUpdateDestroyApiView.as_view(), name='car-detail-update-delete-api'),
    path('api/cars/<int:pk>/comments', CommentListCreateApiView.as_view(), name='comment-create-list-api')
]
