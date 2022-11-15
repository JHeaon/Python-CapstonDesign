from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from gtts import gTTS

from . import translate
from .models import BraiilePicture
from .serializers import BraiilePictureSerializer


class BraiileVeiwSet(viewsets.ModelViewSet):
    queryset = BraiilePicture.objects.all()
    serializer_class = BraiilePictureSerializer

    @action(detail=False, methods=['POST'])
    def set_public(self, request, pk):
        print("hisafddsafasdf")
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)

        return Response("!?!!")
