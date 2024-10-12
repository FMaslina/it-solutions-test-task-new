from rest_framework.serializers import ModelSerializer

from cars.models import Car


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
