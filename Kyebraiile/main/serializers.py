from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, ListField
from .models import BraiilePicture


class BraiilePictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BraiilePicture
        fields = '__all__'


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
