from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new), #데이터를 입력받아서 다른 페이지로 넘기는 것
    path('create/', views.create), 
    #layout은 같은데 컨텐츠만 바뀌게 하는 것/ variable routing/ 게시글을 구분할 수 있는 colum ->id
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),#수정하는 양식이 있는 페이지
    path('<int:pk>/update/', views.update),
]
