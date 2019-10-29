from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new), #데이터를 입력받아서 다른 페이지로 넘기는 것
    path('create/', views.create),
]
