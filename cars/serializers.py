from rest_framework.serializers import ModelSerializer

from cars.models import Car, Comment


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
