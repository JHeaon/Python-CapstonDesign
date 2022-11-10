from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView 
from django.views import View

from gtts import gTTS

from . import translate

class IndexView(APIView):
    
    # 이미지를 구글 tts로 변환하여 전송
    def get(self, request):
        value = translate.PyJsHoisted_analyze_b_(1, "⠣⠒⠉⠻⠚⠠⠝⠬")
        
        
        print()
        
        tts = gTTS(text=value, long='ko')
        return HttpResponse("Hello world!")
    
    
    # 이미지를 받아서 모델돌려 데이터 가공
    def post(self, request):
        return HttpResponse("Hello world!")
    
    
    



