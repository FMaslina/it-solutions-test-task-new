from django.shortcuts import render

from cars.models import Car


def car_list_view(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})
