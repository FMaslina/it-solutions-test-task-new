from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cars.models import Car

from cars.models import Comment

from cars.forms import CommentForm

from cars.forms import CarForm


def car_list_view(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})


def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = Comment.objects.filter(car=car)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.author = request.user
            comment.save()
            return redirect('car-detail', pk=car.pk)
    else:
        form = CommentForm()

    return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})


@login_required
def car_create_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car-list')
    else:
        form = CarForm()

    return render(request, 'car_create.html', {'form': form})


@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.user != car.owner:
        return redirect('car-list')

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car-detail', pk=car.pk)
    else:
        form = CarForm(instance=car)

    return render(request, 'car_edit.html', {'form': form, 'car': car})


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.user == car.owner:
        if request.method == 'POST':
            car.delete()

    return redirect('car-list')
