from django.shortcuts import render, get_object_or_404, redirect

from cars.models import Car

from cars.models import Comment

from cars.forms import CommentForm


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