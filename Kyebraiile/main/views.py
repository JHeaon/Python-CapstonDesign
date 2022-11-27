from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# from gtts import gTTS

from . import translate
from .models import BraiilePicture
from .serializers import BraiilePictureSerializer, UploadSerializer


from .braiile import play
from .translate import PyJsHoisted_analyze_b_
import os


class BraiileVeiwSet(viewsets.ModelViewSet):
    '''
    2가지 설정이 필요
    braiile.py 의 chromedriver의 절대경로
    아래 변수 temp 절대경로 
    '''
    queryset = BraiilePicture.objects.all()
    serializer_class = BraiilePictureSerializer

    @action(detail=True, methods=['GET'])
    def search(self, request, pk):
        temp = "C:/Users/heaon/Desktop/cpst/Python-CapstonDesign/Kyebraiile/media"
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        answer = str(PyJsHoisted_analyze_b_(1, play(full_name)))
        os.remove(full_name)

        return Response(answer)


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(
            content_type)
        return Response(response)
