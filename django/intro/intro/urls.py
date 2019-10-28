"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from pages import views #pages라는 폴더에 views라는 파일

urlpatterns = [ #list형태, 주소의 순서도 중요함. 위에서부터 아래로 검색됨.

    #권장사항 setting.py에 installed_apps 저장 된 순서 대로 하는 것이 좋다.
    path('utils/', include('utils.urls')),
    path('pages/', include('pages.urls')), #파일 자체를 포함시켜야함. views에 있는 함수가 아님.
    path('admin/', admin.site.urls), #문자열,admin.site.urls 여기서 미리 만들어놓은 곳 #전체 url을 총괄하는 폴더
   
]
