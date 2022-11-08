from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Statchung API", # 제목
        default_version='v1', # 버전 
        description="Test description", # 상세 설명 
        terms_of_service="https://www.google.com/policies/terms/", # 개인 정보 약관
        contact=openapi.Contact(email="contact@snippets.local"), # 개발자 연락
        license=openapi.License(name="BSD License"), # 라이 센스 
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls), # url 경로 추가하시면 됩니다. 
    path("", include("main.urls")),
] 

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]