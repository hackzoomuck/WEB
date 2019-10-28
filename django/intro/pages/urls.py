from django.urls import path
#from pages import views #pages에 있는 views.py 앱 import해와라=> 이미 들어와있으니
from . import views 

urlpatterns = [ #list형태, 주소의 순서도 중요함. 위에서부터 아래로 검색됨.
    path('index/', views.index), #views.py 있는 index라는 함수로 접근하겠다. @app.route에 해당
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),#<>동적으로 변하는 값, 마지막 끝에 /로 닫기.
    path('hello_intro/<str:name>/<int:old>/',views.hello_intro),
    path('mul/<int:x>/<int:y>/',views.mul),
    path('dtl/', views.dtl),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto_throw/', views.lotto_throw),
    path('lotto_catch/', views.lotto_catch),
    path('article_new/', views.article_new),
    path('article_create/',views.article_create),
    path('static_example/', views.static_example),
]
