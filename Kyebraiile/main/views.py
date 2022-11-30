# Django import
from django.shortcuts import render

# Drf import
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# 사용자 모듈 import
from .models import BraiilePicture
from .serializers import BraiilePictureSerializer
from .braiile import play
from .translate import PyJsHoisted_analyze_b_
import os


def index_view(request):
    if request.method == 'POST':
        BP = BraiilePicture()
        BP.image = request.FILES["images"]
        BP.save()
        full_name = BraiilePicture.objects.all()
        return render(request, 'index.html', {'full_name': full_name})

    elif request.method == 'GET':
        return render(request, 'index.html')


class BraiileVeiwSet(viewsets.ModelViewSet):
    '''
    2가지 설정이 필요
    1. braiile.py 의 chromedriver의 절대경로 변경해주기 
    2. 아래 변수 temp 절대경로 
    '''
    queryset = BraiilePicture.objects.all()
    serializer_class = BraiilePictureSerializer

    @action(detail=True, methods=['GET'])
    def search(self, request, pk):

        # 사진 쌓이는것 방지 (메모리 관련 문제)
        temp = "C:/Users/heaon/Desktop/cpst/Python-CapstonDesign/Kyebraiile/media"
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        answer = str(PyJsHoisted_analyze_b_(1, play(full_name)))
        os.remove(full_name)

        # DB 삭제
        BraiilePicture.objects.all().delete()

        return render(request, 'index.html', {"answer": answer})
