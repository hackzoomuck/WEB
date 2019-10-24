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
from django.urls import path
from pages import views #pages라는 폴더에 views라는 파일

urlpatterns = [ #list형태, 주소의 순서도 중요함. 위에서부터 아래로 검색됨.
    path('admin/', admin.site.urls), #문자열,admin.site.urls 여기서 미리 만들어놓은 곳
    path('index/', views.index), #views.py 있는 index라는 함수로 접근하겠다. @app.route에 해당
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),#<>동적으로 변하는 값, 마지막 끝에 /로 닫기.
    path('hello_intro/<str:name>/<int:old>/',views.hello_intro),
    path('mul/<int:x>/<int:y>/',views.mul),
    path('dtl/', views.dtl),
    path('birthday/', views.birthday),
]
