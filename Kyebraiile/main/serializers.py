from rest_framework import serializers
from .models import BraiilePicture


class BraiilePictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BraiilePicture
        fields = '__all__'
