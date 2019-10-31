from django.urls import path
from . import views

#새로운 변수
app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new/', views.new, name = 'new'), #데이터를 입력받아서 다른 페이지로 넘기는 것 # GET,POST /articles/new/
    #path('create/', views.create, name = 'create'),  #RESTful하지는 않음(x) 
    #layout은 같은데 컨텐츠만 바뀌게 하는 것/ variable routing/ 게시글을 구분할 수 있는 colum ->id
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),#수정하는 양식이 있는 페이지
   # path('<int:pk>/update/', views.update, name = 'update'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
]

#URL Name -> 각각의 path
#path('주소/', views.함수, name='이름' )
# {% url 'url 이름' %} => /students/new/
# [장점]
# 1. 주소의 변경이 필요할 때, urls.py에서만 수정해주면 됨.
# 2. 마지막 '/'를 빼먹는 실수를 차단할 수 있음.

#APP Name - 특정 app의 urls.py 자체
# {% url 'articles:index'%}
# {% url 'app_name:path_name'%}

#RESTful

#Django는 PUT/PATCH/DELETE 불가능하기에
#GET /articles/2/edit #=> 수정 페이지 보여줌
#POST /articles/edit #=> 수정 작업 수행
#웹프레임워크는 두 메소드를 다르게 받아드림. 구분.

#ex)
#GET /users/1 유저1번 가져옴
#PUT /users/1 유저1번 수정
#DELETE /users/1 유저1번 삭제
