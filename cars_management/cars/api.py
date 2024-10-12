from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cars.models import Car, Comment
from cars.serializers import CarModelSerializer, CommentModelSerializer


class CarRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarModelSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        car = self.get_object()

        if car.owner != request.user:
            return Response({"data": "У вас нет прав на удаление этого автомобиля"},
                            status=status.HTTP_403_FORBIDDEN)

        else:
            self.perform_destroy(car)
            return Response({"data": "Запись о автомобиле успешно удалена"}, status=status.HTTP_200_OK)


class CarListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            new_car = Car.objects.create(make=request.data['make'],
                                         model=request.data['model'],
                                         year=request.data['year'],
                                         description=request.data['description'],
                                         owner=request.user)
        except KeyError:
            return Response({"data": "Недостаточно данных"}, status=status.HTTP_400_BAD_REQUEST)

        serialized_data = self.serializer_class(new_car).data

        return Response(serialized_data, status=status.HTTP_201_CREATED)


class CommentsListByCarApiView(generics.ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Comment.objects.filter(car_id=car_id)


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        car_id = self.kwargs['pk']
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            raise NotFound('Автомобиль не найден')

        serializer.save(car=car, author=self.request.user)
